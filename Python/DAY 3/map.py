# MAP IN PYTHON

# 1. Map with array
arr = [1, 2, 3, 4, 5, 6]

def cube(n):
    return n * n * n

cube_number_iterator = map(cube, arr)
cube_number = list(cube_number_iterator)
print(cube_number)

# 2. Map with set and lambda function
set_list = (1, 2, 3, 4)
res = map(lambda x: x * x, set_list)
square_list = set(res)
print(square_list)


# 3. Passing multiple iteraors to map() using lambda
num1_list = [1, 2, 3, 4, 5]
num2_list = [1, 2, 3, 4, 5]

res = map(lambda n1, n2: n1 + n2, num1_list, num2_list)
final_res = list(res)
print(final_res)

