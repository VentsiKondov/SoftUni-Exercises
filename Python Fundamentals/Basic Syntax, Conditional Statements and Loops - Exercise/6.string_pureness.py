number = int(input())
Pureness = True
for i in range(number):
    word = input()
    letters = list(word)
    for char in letters:
        if char == "." or char == "_"  or char == "," :
            Pureness = False
            break
        else:
            Pureness = True
    if Pureness:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')




