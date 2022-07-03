from cgitb import reset
import numbers
from unittest import result


def bubble_sort(arr):
    array_size = len(arr)

    for iter_num in range(array_size-1):
        swapped = False
        for element in range(array_size-1-iter_num):
            if arr[element] > arr[element+1]:
                arr[element],arr[element+1] = arr[element+1],arr[element]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    numbers = [4,6,8,44,9,55,33]
    sorted_num = [1,2,3,4,5,6,7,8,9]
    sort_string = ['sobit','nayan','furkan','pragyan','ravi','nilesh']

    bubble_sort(sorted_num)
    bubble_sort(numbers)
    bubble_sort(sort_string)
    
    print(numbers)
    print(sorted_num)
    print(sort_string)