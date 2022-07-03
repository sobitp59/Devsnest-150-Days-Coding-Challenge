# found a value in a list, if it exist return it's index and if not return None

def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return  None

def verify(index):
    if index is not None:
        print("The target found at index : ",index)
    else:
        print("Target does not exist")



numbers = [1,2,3,4,5,6,7,8,9,10]
answer = linear_search(numbers,7)
verify(answer)


# print(a)
