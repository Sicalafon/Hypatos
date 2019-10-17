import unittest

from hello_world.formater import plain_text, plain_text_upper_case, plain_text_lower_case

class TestFormater(unittest.TestCase):

    def test_plain_Concationation(self):
        r = plain_text("Hocki", "Klocki Myszka Miki")
        self.assertEqual(r, "Klocki Myszka Miki Hocki", "Błędna konkatynacja tekstu")

    def test_plain_TrimSpaces(self):
        a = plain_text("Hocki", "Klocki  Myszka         Miki")
        self.assertEqual(a, "Klocki Myszka Miki Hocki")

    def test_plain_TrimNewLines(self):
        myString = plain_text("spaces, new lines \n and tabs \t","I want to Remove all white \t")
        self.assertEqual(myString, "I want to Remove all white spaces, new lines and tabs")

    def test_plain_CheckNumbersAndStringsConcatination(self):
        r = plain_text(9.5, "Hocki     Klocki Myszka Miki")
        self.assertEqual(r, "Hocki Klocki Myszka Miki 9.5")


    def test_plain_CheckLists(self):
        r = plain_text("/", [1,3,4])
        r = " ".join(r.split())
        self.assertEqual(" ".join(r.split()), "[1, 3, 4] /")

    def test_plain_upercase_ReturnUpperCase(self):
        r = plain_text_upper_case("test    ", "test ")
        self.assertEqual(r,"TEST TEST")

    def test_plain_upercase_CheckIfUnicodes(self):
        r = plain_text_upper_case("\u0394", "\u0395")
        self.assertEqual(r," ")

    def test_plain_lowercase(self):
        r = plain_text_lower_case("\u0394", "\u0395")
        self.assertEqual(r, r" ")

def json(self):
        pass
