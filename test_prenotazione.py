import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def crea(self, inizio="09:00", fine="10:30", giorno=None):
        return Prenotazione(
            "A1", giorno or date(2026, 11, 26),
            inizio, fine, "Mario", 5
        )

    def test_inizio_non_multiplo_di_30(self):
        with self.assertRaises(ValueError):
            self.crea(inizio="09:15")

    def test_inizio_prima_dell_apertura(self):
        with self.assertRaises(ValueError):
            self.crea(inizio="00:00", fine="01:00")

    def test_fine_dopo_la_chiusura(self):
        with self.assertRaises(ValueError):
            self.crea(inizio="22:00", fine="23:59")

    def test_fine_non_successiva_all_inizio(self):
        with self.assertRaises(ValueError):
            self.crea(inizio="10:00", fine="10:00")

    def test_giorno_non_date(self):
        with self.assertRaises(TypeError):
            self.crea(giorno="26/11/2026")

    def test_durata_minuti(self):
        prenotazione = self.crea("09:00", "10:30")
        self.assertEqual(prenotazione.durata_minuti(), 90)


if __name__ == "__main__":
    unittest.main()
