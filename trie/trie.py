# trie/trie.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Yeh function ek word ko Trie mein insert karta hai.
        """
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Yeh function check karta hai ki word Trie mein exist karta hai ya nahi.
        """
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Yeh function prefix se start hone wale words return karta hai.
        """
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        
        suggestions = []
        self._dfs(node, prefix, suggestions)
        return suggestions

    def _dfs(self, node, prefix, results):
        if len(results) >= 5:
            return
        if node.is_end_of_word:
            results.append(prefix)
        for char in node.children:
            self._dfs(node.children[char], prefix + char, results)
