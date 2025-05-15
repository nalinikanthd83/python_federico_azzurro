print(1, 2, True, ['a', 'b']) #OUTPUT: 1 2 True ['a', 'b']
# By default, it prints them out with a space in between each one of them

print('A', 'B', 'C', sep='')  #OUTPUT: ABC
print('A', 'B', 'C', sep='-') #OUTPUT: A-B-C
print('A', 'B', 'C', sep=' . ') #OUTPUT: A . B . C

print('A', 'B', 'C', sep='-', end='#$\n')
print('Bob', end='@@@@\n')
print('Hello World')
#OUTPUT
# A-B-C#$
# Bob@@@@
# Hello World

print('A', 'B', 'C', end='')
print('Bob')
#OUTPUT
# A B CBob

people: list[str] = ['Mario', 'James', 'Hannah']
print(people)  #OUTPUT:  ['Mario', 'James', 'Hannah']
print(*people) #OUTPUT: Mario James Hannah
# Unpacking took place
print(*people, sep=', ', end='.')  #OUTPUT: Mario, James, Hannah.


