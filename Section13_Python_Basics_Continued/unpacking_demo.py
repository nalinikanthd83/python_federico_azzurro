a = 10, 15
print(type(a)) #OUTPUT: <class 'tuple'>
print(a)       #OUTPUT: (10, 15)

c,d = 20, 25
print(c, d)   #OUTPUT: 20 25

a,b = [30, 35]
print(a, b)  #OUTPUT: 30 35

a, b = 'XY'
print(a, b)  #OUTPUT: X Y

#a,b = 'abcdef'
#print(a, b) #Trimmed output: ValueError: too many values to unpack (expected 2)

a, *b = 'abcdef'
print(a, b) #OUTPUT: a ['b', 'c', 'd', 'e', 'f']

a, *b, c = 'abcdef'
print(a, b, c) #OUTPUT: a ['b', 'c', 'd', 'e'] f

a, b, *c = 'abcdef'
print(a, b, c) #OUTPUT: a b ['c', 'd', 'e', 'f']

a, b, *c, d = 'abcdef'
print(a, b, c, d) #OUTPUT: a b ['c', 'd', 'e'] f

*_, last = 'abcdef'
print(last)      #OUTPUT: f
print(_)         #OUTPUT: ['a', 'b', 'c', 'd', 'e']
# As a convention, if you don't care about a value, you will use the underscore.
# In general, when you use an underscore in Python, you're telling the developer
# or whoever is looking at your code that that value is not important.
# It's just a convention for ignoring the value.

def add(a: int, b: int) -> None:
    print(f'{a+b = }')

add(5, 10)    #OUTPUT: a+b = 15

numbers: dict[str, int] = {'a': 5, 'b': 10}
add(**numbers)      #OUTPUT: a+b = 15

numbers: list[int] = [1, 2, 3, 4, 5]
params: dict[str, str] = {'sep': '-', 'end': '.'}
print(*numbers) #OUTPUT: 1 2 3 4 5
print(*numbers, **params) #OUTPUT: 1-2-3-4-5.

# use this setup throughout our program, we can refer to a single variable.
# To do so, you just need to make sure that these keys exist in whatever
# function you are using.
# Because if something doesn't exist, it's going to raise a type error that it
# is an invalid key argument for that function.




