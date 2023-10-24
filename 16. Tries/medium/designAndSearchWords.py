# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, curr):
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.isEndOfWord
        return dfs(0, self.root)


wd = WordDictionary()
wd.addWord("aa")
wd.addWord("a")
assert wd.search(".") == True
assert wd.search("a") == True
assert wd.search("aa") == True
assert wd.search("aaa") == False
assert wd.search(".a") == True
assert wd.search("a.") == True
