def reverse_array(idx,end,arr):
    if idx == len(arr) // 2:
        return

    arr[idx],arr[end] = arr[end],arr[idx]
    reverse_array(idx+1,end-1,arr)



arr = [int(x) for x in input().split()]
reverse_array(0,-1,arr)


