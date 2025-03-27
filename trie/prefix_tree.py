class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word

    def startsWith(self, prefix: str):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


def main():
    trie = PrefixTree()

    trie.insert("apple")
    trie.insert("orange")

    print(trie.search("apple"))
    print(trie.search("appl"))
    print(trie.startsWith("appl"))
    print(trie.startsWith("pom"))


main()