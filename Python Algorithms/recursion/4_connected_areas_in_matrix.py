def moving(row,col,rows,cols,matrix):
    if row< 0 or row >= rows or col< 0 or col >= cols:
        return 0
    if matrix[row][col] != '-':
        return 0
    matrix[row][col] = 'v'
    result = 1
    result += moving(row,col+1,rows,cols,matrix)
    result += moving(row+1,col,rows,cols,matrix)
    result += moving(row,col-1,rows,cols,matrix)
    result += moving(row-1,col,rows,cols,matrix)
    return result



rows = int(input())
cols = int(input())
my_matrix =[]
for i in range(rows):
    my_matrix.append(list(input()))
arr = []
for row in range(rows):
    for col in range(cols):
        result = moving(row,col,rows,cols,my_matrix)
        if result == 0:
            continue
        arr.append((row,col,result))
print(f'Total areas found: {len(arr)}')
for idx, (r,c,rs) in enumerate(sorted(arr, key=lambda x: x[2], reverse=True)):
    print(f'Area #{idx+1} at ({r}, {c}), size: {rs}')