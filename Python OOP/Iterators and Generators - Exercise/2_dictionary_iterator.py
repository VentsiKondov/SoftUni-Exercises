class dictionary_iter:
    def __init__(self, dictionary:dict):
        self.items = list(dictionary.items())
        self.count = len(dictionary)
        self.step = -1


    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= self.count-1:
            raise StopIteration
        self.step += 1
        return self.items[self.step]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
