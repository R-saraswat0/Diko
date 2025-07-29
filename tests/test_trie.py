import unittest
from trie.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["apple", "app", "application", "bat", "batch", "baton"]
        for word in self.words:
            self.trie.insert(word)

    def test_search_existing_words(self):
        for word in self.words:
            self.assertTrue(self.trie.search(word))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("apples"))
        self.assertFalse(self.trie.search("batman"))
        self.assertFalse(self.trie.search("cat"))

    def test_starts_with(self):
        expected_app = ["app", "apple", "application"]
        result_app = self.trie.starts_with("app")
        self.assertCountEqual(result_app, expected_app)

        expected_bat = ["bat", "batch", "baton"]
        result_bat = self.trie.starts_with("bat")
        self.assertCountEqual(result_bat, expected_bat)

        self.assertEqual(self.trie.starts_with("cat"), [])

if __name__ == "__main__":
    unittest.main()
