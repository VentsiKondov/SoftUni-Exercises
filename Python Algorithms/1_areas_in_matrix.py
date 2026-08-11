rows = int(input())
cols = int(input())
my_matrix = []
my_dict = {}
total = 0
visited = []
for i in range(rows):
    my_matrix.append(list(input()))
    visited.append([False] * cols)


def dfs(key,row, col,matrix,visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return
    if visited[row][col]:
        return
    if my_matrix[row][col] != key:
        return
    visited[row][col] = True
    dfs(key,row - 1, col,matrix,visited)
    dfs(key,row + 1, col,matrix,visited)
    dfs(key,row, col - 1,matrix,visited)
    dfs(key,row, col + 1,matrix,visited)




for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = my_matrix[row][col]
        dfs(key,row, col, my_matrix,visited)
        if my_matrix[row][col] in my_dict:
            my_dict[my_matrix[row][col]] += 1
        else:
            my_dict[my_matrix[row][col]] = 1
        total += 1

print(f'Areas: {total}')
for k,v in sorted(my_dict.items()):
    print(f"Letter '{k}' -> {v}")

