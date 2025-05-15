a: int = 200
b: int = 200

print(a == b) #OUTPUT: True Value comparison
print(a is b) #OUTPUT: True Reference/Identity comparison
# Since it's such a small number, Python stored both a and b in the same point of memory.

a: int = 1000
b: int = int('1000')

print(a == b) #OUTPUT: True Value comparison
print(a is b) #OUTPUT: False Reference/Identity comparison
print(f'{id(a) = }') #OUTPUT: id(a) = 1409893964272
print(f'{id(b) = }') #OUTPUT: id(b) = 1409893970864

var: int | None = None

if var is None: #IMPORTANT: Always use is to compare None. Using == to compare None might not yield correct result
    print('there is no var...')  #OUTPUT: there is no var...
else:
    print(f'Var is: {var}')

class Animal:
    ...

cat = Animal()
dog = Animal()

print(cat is dog) #OUTPUT: False
print(dog is cat) #OUTPUT: False
print(cat is cat) #OUTPUT: True


