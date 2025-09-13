sum_of_ascii = 0


for _ in range(int(input())):
    char = input()
    sum_of_ascii += ord(char)

print(f"The sum equals: {sum_of_ascii}")