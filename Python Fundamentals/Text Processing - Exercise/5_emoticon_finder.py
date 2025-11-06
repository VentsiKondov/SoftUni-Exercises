text = input()

for index, character in enumerate(text):
    if character == ':':
        print(f":{text[index+1]}")

