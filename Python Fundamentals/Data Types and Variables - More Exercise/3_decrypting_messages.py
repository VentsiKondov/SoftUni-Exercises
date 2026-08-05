key = int(input())

list_with_ascii_numbers = []
final_word = []

for _ in range(int(input())):
    char = input()
    ascii_number = ord(char)
    final_word.append(chr(ascii_number + key))

print("".join(final_word))