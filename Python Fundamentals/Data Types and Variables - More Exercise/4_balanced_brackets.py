my_list = []
for _ in range(int(input())):
    some_text = input()
    if some_text == "(" or some_text == ")":
        my_list.append(some_text)


def check_balanced_or_unbalanced(my_list):
    consecutive_brackets = 0
    balanced = False

    if my_list[0] == ")":
        print("UNBALANCED")
        exit()


    for bracket in my_list:
        if bracket == "(":
            consecutive_brackets += 1
            if consecutive_brackets == 2:
                print("UNBALANCED")
                exit()
        elif bracket == ")":
            consecutive_brackets -= 1

    if my_list.count("(") == my_list.count(")"):
        balanced = True
    else:
        balanced = False

    if balanced:
        print("BALANCED")
    else:
        print("UNBALANCED")


check_balanced_or_unbalanced(my_list)


