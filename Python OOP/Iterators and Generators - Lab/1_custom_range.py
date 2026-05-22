class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        while self.count < self.end + 1:
            return self.count
        raise StopIteration

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)