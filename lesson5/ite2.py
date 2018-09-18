from __future__ import print_function

name = raw_input('Please tell me your name: ')
rawAge = raw_input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
    print(name, 'you are 21 years or older!')
    drinkorder = raw_input('What would you like to drink? ')
    print("I'll get you your", drinkorder + '.')
elif age >= 18:
    print('You are allowed in.')
    print('But you are not allowed to drink, please feel free to dance.')
else:
    print('Unfortunately',name,'you are younger than 18.')
