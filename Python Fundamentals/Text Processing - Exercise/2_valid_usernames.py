words = input().split(', ')
correct_words = []
for word in words:
    if 3<=len(word)<=16:

        if word.isalnum() or '-' in word or '_' in word:

            correct_words.append(word)

[print(word) for word in correct_words]
