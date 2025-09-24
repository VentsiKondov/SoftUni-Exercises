def ascii_range(start, end):
    ascii_range = ''
    one =  int(ord(start)+1)
    two = int(ord(end))
    for i in range(one, two):
        print(chr(i), end=" ")
char1 = input()
char2 = input()
ascii_range(char1, char2)