def concatenate(*words,**text):
    unpacked_words = ''.join(words)
    for key in text:
        unpacked_words = unpacked_words.replace(key, text[key])

    return unpacked_words
    




print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))