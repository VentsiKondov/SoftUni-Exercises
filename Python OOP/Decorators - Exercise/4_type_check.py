def type_check(type):
    def decorator(func):
        def wrapper(args):

            if not isinstance(args, type):
                return "Bad Type"
            else:
                return func(args)
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

