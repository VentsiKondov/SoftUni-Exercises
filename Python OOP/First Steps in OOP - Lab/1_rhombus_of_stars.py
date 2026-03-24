rhombus_size = int(input())


def rhombus_maker(rhombus_size):
    for i in range(1, rhombus_size):
        print(" "* (rhombus_size-i) + "* " * i)
    for j in range(rhombus_size, 0,-1):
        print(" "* (rhombus_size-j) + "* "* j)


if rhombus_size == 1:
    print("*")
else:
    rhombus_maker(rhombus_size)

