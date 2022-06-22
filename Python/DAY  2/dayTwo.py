# 🚀 Taking input from the user
"""
name = input('What is your name? ')
print('Welcome ', name)
age = int(input('What is your age? '))
print('Your age : ', age, 'Type of age is : ', type(age))
# inputs take values in string by default, so we may need to typecast
"""

# 🚀 Mutability and immutability

"""
I referred this blog to dive deep in this topic : https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/#M&I

:: LISTS ARE MUTABLE
programmingLanguages = ['Python', 'JavaScript', 'Java ']
for programmingLanguage in programmingLanguages:
    print(programmingLanguage, end=' ')
print(hex(id(programmingLanguages)))

programmingLanguages.append('C++')
for programmingLanguage in programmingLanguages:
    print(programmingLanguage, end=' ')
print(hex(id(programmingLanguages)))

# ids are same before and after which means it doesn't form a new list and hence it is mutable


:: STRINGS ARE IMMUTABLE

name = 'Sobit'
print(name, hex(id(name)))

x = name.replace('Sobit', 'Rohit')
print(x, hex(id(x)))
"""







