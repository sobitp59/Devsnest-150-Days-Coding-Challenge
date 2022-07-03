def search_insert_position(n, arr, key):
    first = 0
    insert_position = first
    last = n-1

    while first <= last:
        midpoint = (first+last)//2
        if arr[midpoint] == key:
            return midpoint
        elif arr[midpoint] < key:
            first = midpoint + 1
            insert_position = first
        else:
            last = midpoint - 1
            insert_position = first
    return insert_position

numbers = [1,2,4,5,6,7,8,9,10]
res = search_insert_position(10,numbers,3)
print(res)

