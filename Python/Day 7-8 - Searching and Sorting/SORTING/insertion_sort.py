def insertion_sort(arr):
    for i in range(1,len(arr)):
        current_elem = arr[i]
        position_pointer = i-1

        while position_pointer >= 0 and current_elem < arr[position_pointer]:
            arr[position_pointer+1] = arr[position_pointer]
            position_pointer = position_pointer - 1
        arr[position_pointer+1] = current_elem

if __name__ == '__main__':
    numbers = [3,2,4,55,22,23,77,66,22]
    insertion_sort(numbers)
    print(numbers)

    # [2, || 1,3,4,55,6,22,13,43]
    # [2, 4, || 3,4,55,6,22,13,43]