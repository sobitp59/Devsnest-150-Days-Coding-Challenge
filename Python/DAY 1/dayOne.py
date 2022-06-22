# Multiple Variable Assignment
"""
a, b, c = 1, 2, 3
print(a, b, c)
"""


# PLAYING WITH MEMORY LOCATIONS
"""
x = 5
y = 20
print(id(x))
print(id(y))

x = 20
y = x
print(y)
print(id(x))
print(id(y))
"""

# STRINGS

 # multiplying strings
name = 'Sobit'
print(name*5)
print(type(name))

# slicing strings
codeAt = 'devsnestBootcamp'
# [a:b:c]  where a = start index, b = stop index, c = step size
print(codeAt[0:4])  # Output : devs
print(codeAt[2:6:2])  # Output : vn
print(codeAt[::-1])  # Output : pmactooBtsensved
print(codeAt[:8:1])  # Output : devsnest
print(codeAt[0::2])  # Output : dvnsBocm

# sep and end parameters
print('Hello,', end='Sobit ')
print('World!')

print('Devsnest', 'Bootcamp', sep='_')
