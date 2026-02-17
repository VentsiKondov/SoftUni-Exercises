number_of_rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(number_of_rows)]


def primary_diagonal(matrix, number_of_rows):
    primary_diagonal = []
    for row in range(number_of_rows):
        primary_diagonal.append(matrix[row][row])
    result_first_diagonal = ", ".join(str(x)for x  in primary_diagonal)
    return result_first_diagonal

def secondary_diagonal(matrix, number_of_rows):
    secondary_diagonal = []
    for row in range(number_of_rows):
            secondary_diagonal.append(matrix[row][number_of_rows - 1 - row])
    result_second_diagonal = ", ".join(str(x)for x  in secondary_diagonal)
    return result_second_diagonal



first_diagonal = primary_diagonal(matrix, number_of_rows)
second_diagonal = secondary_diagonal(matrix, number_of_rows)

sum_first_diagonal = sum(int(x) for x in first_diagonal.split(", "))
sum_second_diagonal = sum(int(x) for x in second_diagonal.split(", "))


print(f"Primary diagonal: {first_diagonal}. Sum: {sum_first_diagonal}")
print(f"Secondary diagonal: {second_diagonal}. Sum: {sum_second_diagonal}")


