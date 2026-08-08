def nested_loops_to_recursion(idx,n,arr):
    if idx >= len(arr):
        print(*arr,sep=' ')
        return
    for num in range(1,n+1):
        arr[idx] = num
        nested_loops_to_recursion(idx+1,n,arr)


number = int(input())
my_lst = [None] * number
nested_loops_to_recursion(0,number,my_lst)
