class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word):
         
            #sorts letters of the original word
        sorted_word = sorted(self.word)
            #compares each word in the list
        return [w for w in word if sorted(w) == sorted_word]

listen = Anagram('listen')
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)
    
