class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDict:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word):
        def dfs(j: int, node: TrieNode):
            cur = node

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.end_of_word

        return dfs(0, self.root)


def main():
    wd = WordDict()

    print(wd.search("abcd"))
    wd.insert("apple")
    wd.insert("google")
    wd.insert("lunch")

    print(wd.search("apple"))
    print(wd.search("appl."))
    print(wd.search(".ppl."))

main()