print(locals())
# we will get everything that is local to the global namespace
# So in the outer scope, it essentially makes no difference whether you use the globals or the locals

def add(a: int, b: int) -> None:
    result: int = a + b
    print(f'{a} + {b} = {result}')

    print('add() has: ', locals())

add(1,1)
# add() has:  {'a': 1, 'b': 1, 'result': 2}
# This information is not visible outside the function, it is local to the function.