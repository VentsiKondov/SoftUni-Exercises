first_string, second_string = input().split()

first_len = len(first_string)
second_len = len(second_string)
total_sum = 0

def larger_index_finder(text1,text2):
    if len(text1) > len(text2):
        return len(text1)
    elif len(text1) < len(text2):
        return len(text2)
    return len(text1)

while True:
    for index in range(0, larger_index_finder(first_string, second_string)):
        try:
            first_char = first_string[index]
        except IndexError:
            for char in second_string[index:]:
                total_sum += ord(char)
            break

        try:
            second_char = second_string[index]
        except IndexError:
            for char in first_string[index:]:
                total_sum += ord(char)
            break


        total_sum += (ord(first_char) * ord(second_char))
    break


print(total_sum)




