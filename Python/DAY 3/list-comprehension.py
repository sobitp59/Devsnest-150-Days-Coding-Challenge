#  LIST COMPREHENSION IN PYTHON

# 1. Iterating through a string using Loop

arr = []
for letter in 'sobit':
    arr.append(letter)
print(arr)

# 2. Iterating through a string using list comprehension
arr2 = [letter for letter in 'prasad']
print(arr2)



# 3. Conditionals in List Comprehension

even_num = [x for x in range(1, 21) if x % 2 == 0]
print(even_num)

# 4. If...Else with List Comprehension
even_or_odd = ['It is even' if i % 2 == 0 else 'It is odd' for i in range(101)]
print(even_or_odd)