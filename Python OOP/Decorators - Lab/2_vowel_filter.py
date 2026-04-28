def vowel_filter(function):
    vowels = ['a', 'e', 'i', 'o', 'u']
    def wrapper():
        res = function()
        return [w for w in res if w in vowels]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
