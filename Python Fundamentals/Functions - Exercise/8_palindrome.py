def palindrome_number(numbers):
    for num in numbers:
        if num[0] == num[-1]:
            print("True")
        else:
            print("False")

list_of_numbers = list(map(str, input().split(", ")))
(palindrome_number(list_of_numbers))