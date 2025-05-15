# exec does not return anything, it only executes code while eval evaluates
# that code.

code: str =  '''
x: int = 10
y: int = 20

print(x + y)
print('Hello World!')

for i in range(3):
    print(i)

'''
exec(code)

# OUTPUT:
# 30
# Hello World!
# 0
# 1
# 2

while True:
    user_input1: str = input('Command: ')
    exec(user_input1)

# OUTPUT
# Command: print("hello, james")
# hello, james

# OUTPUT
# Command: print([i for i in range(10)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# IMPORTANT
# Always use exec and eval with caution because it is possible some people can inject
# some pretty nasty code in there that might be able to access your sensitive information.


