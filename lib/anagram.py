# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if self._is_anagram(word.lower())]
    
    def _is_anagram(self, candidate):
        if candidate == self.word:
            return False
        return sorted(candidate) == sorted(self.word)