electrons = int(input())
my_lst = []
n = 1
while True:
    formula = 2*(n**2)
    if electrons >= formula:
        electrons -= formula
        my_lst.append(formula)
    else:
        if electrons != 0:
            my_lst.append(electrons)
        break
    n+=1

print(my_lst)
