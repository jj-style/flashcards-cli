import unittest
import os

from flashcards_cli import Set
from flashcards_cli.flashcard import Flashcard

class TestFlaschards(unittest.TestCase):

    def test_construction(self):
        f = Flashcard("term", "definition")

    def test_eq_positive(self):
        f = Flashcard("term", "definition")
        g = Flashcard("term", "definition")
        self.assertTrue(f==g)
    
    def test_eq_negative(self):
        f = Flashcard("term", "definition")
        g = Flashcard("abc", "def")
        self.assertFalse(f==g)

    def test_eq_type_mismatch(self):
        self.assertFalse(Flashcard("term", "definition") == "term")

    def test_eq_identical(self):
        f = Flashcard("term", "definition")
        self.assertTrue(f==f)

    def test_neq_positive(self):
        f = Flashcard("term", "definition")
        g = Flashcard("abc", "def")
        self.assertTrue(f!=g)
    
    def test_neq_negative(self):
        f = Flashcard("term", "definition")
        g = Flashcard("term", "definition")
        self.assertFalse(f!=g)

    def test_neq_type_mismatch(self):
        self.assertTrue(Flashcard("term", "definition") != "term")

    def test_neq_identical(self):
        f = Flashcard("term", "definition")
        self.assertFalse(f!=f)

class TestSetConstruction(unittest.TestCase):

    def setUp(self):
        self.example_card_one = Flashcard("term", "definition")
        self.example_card_two = Flashcard("term 2", "definition 2")
        self.example_card_three = Flashcard("term 3", "definition 4")

        csv_text = "term,definition\nt1,d1\nt2,d2\nt3,d3\n"
        csv_text2 = "term,definition\nt4,d4\nt5,d5\nt6,d6\n"
        with open("temp.txt","w") as file:
            file.write(csv_text)

        with open("temp2.txt","w") as file:
            file.write(csv_text2)

    def tearDown(self):
        os.remove("temp.txt")
        os.remove("temp2.txt")

    def test_empty(self):
        s = Set("name")
    
    def test_with_list_of_cards(self):
        s = Set("name", cards=[self.example_card_one, self.example_card_two])

    def test_empty_factory(self):
        s = Set.create_empty_set()

    def test_load_from_csv(self):
        s = Set.load_from_csv("temp.txt")

    def test_load_multiple_from_csv(self):
        s = Set.load_from_csv("temp.txt", "temp2.txt")

class TestCollectionProtocols(unittest.TestCase):

    def setUp(self):
        self.example_card_one = Flashcard("term", "definition")
        self.example_card_two = Flashcard("term 2", "definition 2")
        self.example_card_three = Flashcard("term 3", "definition 4")
        
        self.s = Set("set", [self.example_card_one, self.example_card_two, self.example_card_three])

    def test_len_zero(self):
        self.assertEqual(0, len(Set("name")))

    def test_len(self):
        self.assertEqual(3, len(self.s))

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), self.example_card_one)
        self.assertEqual(next(i), self.example_card_two)
        self.assertEqual(next(i), self.example_card_three)
        self.assertRaises(StopIteration, lambda: next(i))
    
    def test_for_loop(self):
        expected = [self.example_card_one, self.example_card_two, self.example_card_three]
        index = 0
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_index_zero(self):
        self.assertEqual(self.example_card_one, self.s[0])
        
    def test_index_two(self):
        self.assertEqual(self.example_card_three, self.s[2])
        
    def test_index_error(self):
        with self.assertRaises(IndexError):
            self.s[3]
        
    def test_index_minus_one(self):
        self.assertEqual(self.example_card_three, self.s[-1])
        
    def test_index_minus_three(self):
        self.assertEqual(self.example_card_one, self.s[-3])
        
    def test_index_error_minus_four(self):
        with self.assertRaises(IndexError):
            self.s[-4]

    def test_eq_positive(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_one])
        self.assertTrue(s == t)

    def test_eq_negative(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_two])
        self.assertFalse(s == t)

    def test_eq_type_mismatch(self):
        self.assertFalse(Set("one",[self.example_card_one]) == [self.example_card_one])

    def test_identical(self):
        s = Set("one", [self.example_card_one])
        self.assertTrue(s == s)

    def test_neq_positive(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_one])
        self.assertFalse(s != t)

    def test_neq_negative(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_two])
        self.assertTrue(s != t)

    def test_neq_type_mismatch(self):
        self.assertTrue(Set("one",[self.example_card_one]) != [self.example_card_one])

    def test_neq_identical(self):
        s = Set("one", [self.example_card_one])
        self.assertFalse(s != s)

    def test_add(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_two])
        self.assertEqual(s+t, Set("one,two",[self.example_card_one, self.example_card_two]))

    def test_add_repeat(self):
        s = Set("one", [self.example_card_one])
        t = Set("two", [self.example_card_two, self.example_card_one])
        self.assertEqual(s+t, Set("one,two",[self.example_card_one, self.example_card_two, self.example_card_one]))

if __name__ == "__main__":
    unittest.main()