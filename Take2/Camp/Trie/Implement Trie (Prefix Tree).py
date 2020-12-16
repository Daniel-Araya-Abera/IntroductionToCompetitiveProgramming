class Node:
    def __init__(self):
        self.letters = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.head
        for letter in word:
            if letter not in curr_node.letters:
                curr_node.letters[letter] = Node()
            
            curr_node = curr_node.letters[letter]
        
        curr_node.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.head
        
        for letter in word:
            if letter not in curr_node.letters:
                return False
            curr_node = curr_node.letters[letter]
        return curr_node.isEnd        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.head
        for letter in prefix:
            if letter not in curr_node.letters:
                return False            
            curr_node = curr_node.letters[letter]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
