class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.words = set()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.words.add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.words:
            if self._match(w, word):
                return True 

        return False 

    def _match(self, word, pat):
        if len(word) != len(pat):
            return False 

        for a, b in zip(word, pat):
            if a == b or b == '.':
                continue 
            else:
                return False   

        return True 
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("pattern")