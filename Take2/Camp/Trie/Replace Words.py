class TrieNode:
    def __init__(self):
        self.letters = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def addWord(self, word):
        curr_node = self.head
        for letter in word:
            if letter not in curr_node.letters:
                curr_node.letters[letter] = TrieNode()

            curr_node = curr_node.letters[letter]

        curr_node.isEnd = True
    
    def searchWord(self, word):
        curr_node = self.head
        resWord = ""
        for i in range(len(word)):
            curr_letter = word[i]
            if curr_letter not in curr_node.letters:
                return False
            else:
                curr_node = curr_node.letters[curr_letter]
            if curr_node.isEnd:
                resWord = word[:i + 1]
                break
        
        return resWord           

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)
        
        words = sentence.split()
        
        for i, word in enumerate(words):
            shorterWordFound =  trie.searchWord(word)
            if shorterWordFound:
                words[i] = shorterWordFound
        
        newSentence = " ".join(words)
        return newSentence
        
