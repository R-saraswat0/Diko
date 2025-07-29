# app/main.py

import os
import sys
sys.path.append("..")  # Sibling folders ko access karne ke liye

from trie.trie import Trie
from corrections.edit import get_closest_words
from scraper.defination import get_definition

def load_words(trie, filepath):
    """
    Yeh function words.txt file se words load karta hai
    aur unhe Trie mein insert karta hai.
    """
    words = []
    with open(filepath, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                words.append(word)
                trie.insert(word)
    return words

def main():
    """
    Main function jo user se input leta hai,
    Trie mein search karta hai, aur definition fetch karta hai.
    """
    print("📘 Welcome to Word Lookup Dictionary!")
    trie = Trie()
    word_file = os.path.join('data', 'words.txt')
    word_list = load_words(trie, word_file)

    while True:
        query = input("\n🔍 Enter word to search (or 'exit'): ").strip()
        if query.lower() == 'exit':
            print("👋 Exiting. Goodbye!")
            break

        if trie.search(query):
            print(f"✅ '{query}' found in dictionary.")
            definition = get_definition(query)
            print(f"📖 Definition: {definition}")
        else:
            print(f"❌ '{query}' not found.")
            suggestions = trie.starts_with(query)
            if suggestions:
                print("🔎 Suggestions from dictionary:", ", ".join(suggestions))
            else:
                close_matches = get_closest_words(query, word_list)
                print("💡 Did you mean:", ", ".join(close_matches))
                # Optionally, fetch definition for first suggestion
                if close_matches:
                    definition = get_definition(close_matches[0])
                    print(f"📖 Definition of '{close_matches[0]}': {definition}")

if __name__ == "__main__":
    main()
