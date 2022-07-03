def merge_sort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        left_half = arr[:midpoint]
        right_half = arr[midpoint:]
        
        merge_sort(left_half)
        merge_sort(right_half)

        left_ptr = right_ptr = arr_ptr = 0

        while left_ptr < len(left_half) and right_ptr < len(right_half):
            if left_half[left_ptr] < right_half[right_ptr]:
                arr[arr_ptr] = left_half[left_ptr]
                left_ptr+=1
            else:
                arr[arr_ptr] = right_half[right_ptr]
                right_ptr+=1
            arr_ptr+=1

        while left_ptr < len(left_half):
            arr[arr_ptr] = left_half[left_ptr]
            left_ptr+=1
            arr_ptr+=1
        while right_ptr < len(right_half):
            arr[arr_ptr] = right_half[right_ptr]
            right_ptr+=1
            arr_ptr+=1
        
        
if __name__ == '__main__':
    num = [22,33,11,44,55,33,55]
    merge_sort(num)
    print(num)

