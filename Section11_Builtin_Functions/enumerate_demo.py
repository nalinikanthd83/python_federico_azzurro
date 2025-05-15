elements: list[str] = ['A', 'B', 'C']
i: int = 0

for element in elements:
    i += 1
    print(f'{i}: {element}')

#OUTPUT
# 1: A
# 2: B
# 3: C

elements: list[str] = ['A', 'B', 'C']
enumeration: enumerate[str] = enumerate(elements)
print(enumeration) #OUTPUT: <enumerate object at 0x000001AF805C99E0>
print(list(enumeration)) #OUTPUT: [(0, 'A'), (1, 'B'), (2, 'C')]

# Creating an enumeration creates a list of tuples

# All our elements will be paired with a number in an increasing order.
# And by default it starts at zero and counts upwards.
# But if you want, you can also specify a start.

elements: list[str] = ['A', 'B', 'C']
enumeration: enumerate[str] = enumerate(elements, start=1)
print(enumeration) #OUTPUT: <enumerate object at 0x00000140E3431E40>
print(list(enumeration)) #OUTPUT: [(1, 'A'), (2, 'B'), (3, 'C')]


elements: list[str] = ['A', 'B', 'C']
for i, element in enumerate(elements):
    print(f'{i}: {element}')
#OUTPUT
# 0: A
# 1: B
# 2: C

elements: list[str] = ['A', 'B', 'C']
for i, element in enumerate(elements, start=1):
    print(f'{i}: {element}')
#OUTPUT
# 1: A
# 2: B
# 3: C







