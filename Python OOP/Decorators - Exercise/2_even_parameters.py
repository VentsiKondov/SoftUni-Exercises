def even_parameters(func):
    def wrapper(*args):
        for num in args:
            if isinstance(num, int) and num % 2 == 0:
                continue
            else:
                return "Please use only even numbers!"
        else:
            return func(*args)
    return wrapper







@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


