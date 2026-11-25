import unittest
from datetime import date

from prenotazioni import Agenda, Sala, Prenotazione


class TestSegnalazioni(unittest.TestCase):
    def test_accetta_prenotazioni_contigue(self):
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A1", "Aula 1", 10))

        oggi = date(2026, 11, 25)
        giorno = date(2026, 11, 26)

        prima = Prenotazione(
            "A1", giorno, "09:00", "10:00", "Mario", 2
        )
        seconda = Prenotazione(
            "A1", giorno, "10:00", "11:00", "Luigi", 2
        )

        agenda.prenota(prima, oggi=oggi)
        agenda.prenota(seconda, oggi=oggi)


    def test_accetta_prenotazione_con_capienza_esatta(self):
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A1", "Aula 1", 10))

        oggi = date(2026, 11, 25)
        giorno = date(2026, 11, 26)

        prenotazione = Prenotazione(
            "A1", giorno, "09:00", "10:00", "Mario", 10
        )

        agenda.prenota(prenotazione, oggi=oggi)

if __name__ == "__main__":
    unittest.main()
