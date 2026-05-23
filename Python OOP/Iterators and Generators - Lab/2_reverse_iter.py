class reverse_iter:
    def __init__(self, iterable):
        self.iterable = sorted(iterable, reverse=True)
        self.index = -1
        self.length = len(iterable) - 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            self.index += 1
            return self.iterable[self.index]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)