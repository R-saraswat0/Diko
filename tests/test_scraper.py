import unittest
from scraper.defination import get_definition

class TestScraper(unittest.TestCase):
    def test_get_definition_valid_word(self):
        result = get_definition("example")
        self.assertIn("word", result)
        self.assertEqual(result["word"].lower(), "example")
        self.assertIn("meanings", result)
        self.assertIsInstance(result["meanings"], list)

    def test_get_definition_invalid_word(self):
        result = get_definition("asldkfjalskdfj")  # likely invalid word
        self.assertTrue("error" in result or "word" in result)

if __name__ == "__main__":
    unittest.main()
