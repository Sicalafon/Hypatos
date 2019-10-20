import unittest
import sqlite3

conn = sqlite3.connect("performed_test.db")
c= conn.cursor()


def insert(table, record1, record2):
    c.execute("""INSERT INTO {} (TEST, RESULTS) VALUES ('{}','{}')""".format(table, record1, record2))

def delete_table(table):
    c.execute("""DROP TABLE {} """.format(table))

def truncate_table(table):
    c.execute("""DELETE FROM {}""".format(table))
    c.execute("""delete from sqlite_sequence where name='{}';""".format(table))


c.execute("""
CREATE TABLE if not exists PERFORMED_TESTS (ID integer primary key autoincrement, TEST TEXT, RESULTS TEXT)
""")



conn.commit()




from hello_world.formater import plain_text, plain_text_upper_case, plain_text_lower_case, format_to_json

class TestFormater(unittest.TestCase):

    def test_plain_Concationation(self):
        r = plain_text("Hocki", "Klocki Myszka Miki")
        try:
           self.assertEqual(r, "Klocki Myszka Miki Hocki")
           insert("PERFORMED_TESTS", self._testMethodName, "Test passed")
        except:
           insert("PERFORMED_TESTS", self._testMethodName, "Test failed")

        c.execute("SELECT * FROM PERFORMED_TESTS")
        print(c.fetchall())

        conn.commit()

    def test_plain_TrimSpaces(self):
        r = plain_text("Hocki", "Klocki  Myszka         Miki")
        try:
           self.assertEqual(r, "Klocki Myszka Miki Hocki")
           insert("PERFORMED_TESTS", self._testMethodName, "Test passed")
        except:
           insert("PERFORMED_TESTS", self._testMethodName, "Test failed")


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

    def test_json_if_valid(self):
           r = format_to_json("Cześć","Bartek")
           self.assertEqual(r,"""{ "imie":"Bartek", "mgs":"Cześć"}""")

    def test_json_if_load(self):
           import json
           r = format_to_json("Cześć","Bartek")
           self.assertTrue(json.loads(r))

    def test_json_special_characters(self):
        r = format_to_json(imie='Bartek { "Bart" \ Tyrała',msg='Czesc')
        self.assertEqual(r,r"""{ "imie":"Bartek \{ \"Bart\" \\ Tyrała", "mgs":"Czesc"}""")





# conn.close()
