numbers: list[int] = [1, 2, 3, 4, 5]

def double(number: int) -> int:
    return number * 2

doubled: map = map(double, numbers)
print(doubled) #OUTPUT: <map object at 0x00000251D2064C10>
print(list(doubled)) #OUTPUT: [2, 4, 6, 8, 10]

doubled: map = map(lambda number: number * 2, numbers)
print(doubled) #OUTPUT: <map object at 0x0000019216F14160>
print(list(doubled)) #OUTPUT: [2, 4, 6, 8, 10]

numbers: list[int] = [1, 2, 3, 4, 5]
letters: list[str] = ['a', 'b', 'c']

def combine_elements(n: int, l: str) -> tuple[int, str]:
    return n, l

combined: map = map(combine_elements, numbers, letters)
print(list(combined)) #OUTPUT: [(1, 'a'), (2, 'b'), (3, 'c')]

combined: map = map(lambda n, l: (n, l), numbers, letters)
print(list(combined)) #OUTPUT: [(1, 'a'), (2, 'b'), (3, 'c')]

# It will stop as soon as the shortest list runs out of elements.
# Because our numbers contained five elements, while our letters contained only three.
# So once it ran out of elements to use in the shortest list, it just stopped there because it had no
# idea what to do with the rest of the elements.

