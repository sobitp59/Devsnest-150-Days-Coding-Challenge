def selection_sort(arr):
    arr_size = len(arr)

    for i in range(arr_size-1):
        min_index = i
        for j in range(min_index+1, arr_size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [22,44,1,4,2,55,88,6]
selection_sort(numbers)
print(numbers)