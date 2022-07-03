def binary_search(n, list, target):
    first = 0
    last = n - 1

    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None

numbers = [1,2,4,5,6,7,8,9,10]

result = binary_search(10,numbers,3)

print(result)
