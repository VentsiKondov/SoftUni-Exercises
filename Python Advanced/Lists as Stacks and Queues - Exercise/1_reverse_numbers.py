# stack = input().split()
# print(" ".join(stack[::-1]))
my_stack = list(map(int, input().split()))
while len(my_stack):
    print(my_stack.pop(), end=" ")

