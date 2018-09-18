from __future__ import print_function

name = raw_input('Please tell me your name: ')
rawAge = raw_input('Please tell me your age: ')
age = int(rawAge)

if age >= 19:
    print(name, 'you are 19 years or older!')
    drinkorder = raw_input('What would you like to drink? ')
    print("I'll get you your", drinkorder + '.')
else:
    print('Unfortunately',name,'you are younger than 19.')
