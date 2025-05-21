
def func(var_a: str, /, var_b: str) -> None:
    print(var_a)
    print(var_b)

func('a', var_b = 'b')
# Everything in front of the slash must be passed in as a positional argument

# func(var_a = 'a', var_b = 'b')
# TypeError: func() got some positional-only arguments passed as keyword arguments: 'var_a'

def func(var_a: str, *, var_b: str) -> None:
    print(var_a)
    print(var_b)

# func('a', var_b='b')
# Everything after * must be passed in as a keyword argument

def func1(var_a: str, /, var_b: str, *, var_c: str) -> None:
    print(var_a)
    print(var_b)
    print(var_c)

func1('a', 'b', var_c='c')
# a
# b
# c

func1('a', var_b='b', var_c='c')
# a
# b
# c

func1(var_a='a', var_b='b', var_c='c')
# TypeError: func1() got some positional-only arguments passed as keyword arguments: 'var_a'