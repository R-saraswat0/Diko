import unittest
from corrections.edit import edit_distance, get_closest_words

class TestCorrections(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("flaw", "lawn"), 2)
        self.assertEqual(edit_distance("intention", "execution"), 5)
        self.assertEqual(edit_distance("", ""), 0)
        self.assertEqual(edit_distance("a", ""), 1)
        self.assertEqual(edit_distance("", "a"), 1)

    def test_get_closest_words(self):
        word_list = ["apple", "apply", "ape", "banana", "band", "bandana"]
        query = "aple"
        expected = ["apple", "apply", "ape"]
        result = get_closest_words(query, word_list, top_n=3)
        self.assertEqual(result, expected)

        query2 = "banda"
        expected2 = ["band", "bandana", "banana"]
        result2 = get_closest_words(query2, word_list, top_n=3)
        self.assertEqual(result2, expected2)

if __name__ == "__main__":
    unittest.main()
