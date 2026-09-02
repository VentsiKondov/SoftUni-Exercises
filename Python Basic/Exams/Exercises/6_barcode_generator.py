first_number = input()
second_number = input()

first_d, second_d, third_d, fourth_d= int(first_number[0]),int(first_number[1]),int(first_number[2]),int(first_number[3])
first_n, second_n, third_n, fourth_n= int(second_number[0]),int(second_number[1]),int(second_number[2]),int(second_number[3])

for x1 in range(first_d, first_n+1):
        if x1 % 2 ==0:
            continue

        for x2 in range(second_d, second_n+1):
            if x2 % 2 ==0:
                continue
            for x3 in range(third_d, third_n+1):
                if x3 % 2 ==0:
                    continue
                for x4 in range(fourth_d, fourth_n+1):
                    if x4 % 2 ==0:
                        continue
                    print(f"{x1}{x2}{x3}{x4}", end=" ")


