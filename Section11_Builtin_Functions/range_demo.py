my_range: range = range(1, 6)
print(my_range) # range(1, 6)
print(list(my_range)) # [1, 2, 3, 4, 5]

my_range: range = range(6)
print(my_range) # range(0, 6)
print(list(my_range)) # [0, 1, 2, 3, 4, 5]

my_range: range = range(0, 10, 2)
print(my_range) # range(0, 10, 2)
print(list(my_range)) # [0, 2, 4, 6, 8]

my_range: range = range(-5)
print(my_range) # range(0, -5)
print(list(my_range)) # []

my_range: range = range(-5, 0)
print(my_range) # range(-5, 0)
print(list(my_range)) # [-5, -4, -3, -2, -1]

my_range: range = range(0, -5)
print(my_range) # range(0, -5)
print(list(my_range)) # []

my_range: range = range(0, -5, -1)
print(my_range) # range(0, -5, -1)
print(list(my_range)) # [0, -1, -2, -3, -4]

for i in range(4):
    print(f'{i}')
# 0
# 1
# 2
# 3

# IMPORTANT:
# The nice thing about iterables,
# such as ranges and enumerations, is that we do not need to convert
# it to a list or to a tuple before looping through it


