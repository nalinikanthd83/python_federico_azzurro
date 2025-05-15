numbers = list(range(1, 21))
print(numbers)  # OUTPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def is_even(number: int) -> bool:
    return number % 2 == 0


even_numbers: filter = filter(is_even, numbers)
print(even_numbers)  # OUTPUT: <filter object at 0x00000278AB324C10>
print(list(even_numbers))  # OUTPUT: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

even_numbers: filter = filter(lambda n: n % 2 == 0, numbers)
print(even_numbers)  # OUTPUT: <filter object at 0x0000013FCBFF41C0>
print(list(even_numbers))  # OUTPUT: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

people: list[str] = ['Anna', 'Bob', 'Betty', 'James', 'John']
long_names: filter = filter(lambda name: len(name) > 4, people)
print(list(long_names)) #OUTPUT: ['Betty', 'James']

ln: list[str] = [name for name in people if len(name) > 4]
print(ln) #OUTPUT: ['Betty', 'James']

# IMPORTANT - difference between list comprehension and filter object

# The only thing to note here is that filter returns an incredibly memory efficient object, while our
# list comprehension returns a list directly.
# So if you have millions of elements in general, you might want to use filter, because filter will
# return that memory efficient object that does not load everything into memory immediately, while a
# list comprehension will load that into memory immediately.
