result: int = eval('1 + 2 + 100')
print(result) #OUTPUT: 103

x: int = 5
y: int = 10

print(eval('x + y')) #OUTPUT: 15

while True:
    user_input: str = input('Enter math: ')
    print(eval(user_input))

    #OUTPUT:
    # Enter math: 10 + 10
    # 20

    # OUTPUT:
    # Enter math: print('hello')
    # hello
    # None

# It's okay to use in your personal projects, but if you ever create a product that uses it, you need
# to really think hard about how to prevent users from actually injecting code into your script.