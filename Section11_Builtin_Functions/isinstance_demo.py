# isinstance() - It checks if an object is an instance of another object
# or even a subclass of another object

number: int = 100
pi: float = 3.14
text: str = 'Hello'
my_list: list[int] = [1, 2, 3, 4]

print(isinstance(number, int)) # True
print(isinstance(number, str)) # False
print(isinstance(pi, int))     # False
print(isinstance(my_list, int | float | str | tuple | list)) # True
# | acts as UnionType above

class Animal:
    pass

class Cat(Animal):
    ...

print(isinstance(Cat(), Animal)) # True
print(isinstance(Animal(), Cat)) # False (IMPORTANT)





