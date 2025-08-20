entry_n = int(input())
exit_n = int(input())
magic_num = int(input())
counter = 0
all_combinations = 0
is_found = False

for i in range(entry_n, exit_n + 1):
    for j in range(entry_n, exit_n + 1):
        counter += 1
        if i + j ==magic_num or j + i == magic_num:
            is_found = True
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            exit()
        all_combinations += 1

if not is_found:
    print(f"{all_combinations} combinations - neither equals {magic_num}")


