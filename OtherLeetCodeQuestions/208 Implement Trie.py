#TODO: I dont understand this code
class TrieClass:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie

        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]

        trie['$'] = True

    def search(self, word: str) -> bool:
        trie = self.trie

        for c in word:
            if c not in trie:
                return False
            trie = trie[c]

        if '$' in trie:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie

        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]

        return True

sln = TrieClass()
print(sln.search(("Snowy")))
print(sln.insert("Satvik"))
print(sln.insert("Suhaas"))
print(sln.startsWith("Su"))
print(sln.startsWith("Sa"))
