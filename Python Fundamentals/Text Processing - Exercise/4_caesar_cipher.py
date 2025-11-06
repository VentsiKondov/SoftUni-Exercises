text = input()
ascii_text = []

for char in text:
    ascii_number = ord(char)
    ascii_text.append(chr(ascii_number+3))

print(''.join(ascii_text))