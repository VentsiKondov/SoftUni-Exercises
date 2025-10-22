secret_message = input().split()
number_lst = []
num = ''
new_word = []
for word in secret_message:
    digit_lst = [digit for digit in word if digit.isdigit()]
    letter_list = [letter for letter in word if letter.isalpha()]
    num = ''.join(digit_lst)
    letter_list[0], letter_list[-1] = letter_list[-1], letter_list[0]
    new_word.append(chr(int(num)) + ''.join(letter_list))

print(" ".join(new_word))










