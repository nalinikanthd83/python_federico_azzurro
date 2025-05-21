
def add(*args: int) -> int:
    print(args)
    return sum(args)

print(add(1, 2, 3, 10, 14, 21))
# (1, 2, 3, 10, 14, 21)
#51

print(add())
# ()
# 0 because sum() function returns sum of start value (default: 0)


def add1(*args: int) -> int:
    sum: int = 0
    if len(args) > 0:
        for i in args:
            sum += i
    return sum

print(add1(1, 5, 8, 12)) #26

# values passed will ve stored as a tuple with name args

# we can use any name instead of args
def add2(*numbers: int) -> int:
    sum: int = 0
    if len(numbers) > 0:
        for i in numbers:
            sum += i
    return sum

print(add2(1, 5, 8, 12)) #26

def greet(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f'{greeting}, {person}{ending}')

greet('Hello', 'Bob', 'James', 'Maria', ending='!')
# Hello, Bob!
# Hello, James!
# Hello, Maria!

# IMPORTANT
# Although it works, avoid putting positional arguments in front of variable positional arguments

def pin_postion(**kwargs: int) -> None:
    print(kwargs)


pin_postion(x=10, y=20)
# {'x': 10, 'y': 20}

def func(*args: str, **kwargs: int) -> None:
    print(args)
    print(kwargs)

func('a', 'b', a=1, b=2)
# ('a', 'b')
# {'a': 1, 'b': 2}

def func(*args: str, default: int, **kwargs: int) -> None:
    print(args)
    print(kwargs)
    print(default)

func('a', 'b', default=20, a=1, b=2)
# ('a', 'b')
# {'a': 1, 'b': 2}
# 20

func('a', 'b', 20, a=1, b=2)
# TypeError: func() missing 1 required keyword-only argument: 'default'


