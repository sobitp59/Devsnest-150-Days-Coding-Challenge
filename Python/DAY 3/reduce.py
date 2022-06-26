import functools

# Reduce in Python
list_num = [1, 2, 3, 4, 5]
print('The sum is: ', end='')
print(functools.reduce(lambda a, b: a+b, list_num))

