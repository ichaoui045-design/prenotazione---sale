import unittest
from datetime import date

from prenotazioni import (
    Agenda,
    Sala,
    Prenotazione,
    SalaNonTrovata,
    DataNonAmmessa,
    PrenotazioneNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A1", "Sala A", 20))
        self.oggi = date(2026, 11, 25)

    def crea(self, giorno=None, codice="A1"):
        return Prenotazione(
            codice, giorno or self.oggi, "09:00", "10:00", "Mario", 5
        )

    def test_codice_sala_duplicato(self):
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(Sala("A1", "Altra sala", 10))

    def test_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("X")

    def test_data_passata(self):
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(
                self.crea(date(2026, 11, 24)), oggi=self.oggi
            )

    def test_domenica_non_ammessa(self):
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(
                self.crea(date(2026, 11, 29)), oggi=self.oggi
            )

    def test_oltre_orizzonte(self):
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(
                self.crea(date(2027, 2, 1)), oggi=self.oggi
            )

    def test_accetta_oggi(self):
        identificativo = self.agenda.prenota(
            self.crea(), oggi=self.oggi
        )
        self.assertEqual(identificativo, 1)

    def test_cancella_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(999)

    def test_prenotazione_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(999)


if __name__ == "__main__":
    unittest.main()
