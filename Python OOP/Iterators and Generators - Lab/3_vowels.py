class vowels:
    vowel = ['a', 'e', 'i', 'o', 'u','y']
    def __init__(self, word):
        self.word = word
        self.index = -1
        self.length = len(word) - 1

    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index > self.length:
            raise StopIteration
        if self.word[self.index].lower() in self.vowel:
            return self.word[self.index]
        else:
            return self.__next__()






my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)