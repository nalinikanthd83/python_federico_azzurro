
def greet(name: str) -> None: # name in function declaration is parameter
    print(f'{name}')

greet('Bob')  # Bob is the argument we are passing to the function
# Bob

def greeting(name: str, language: str, default: str):
    if language == 'it':
        print(f'hello {name}')
    else:
        print(f'{default} {name}')

greeting('Mario', 'it', 'hi')
#OUTPUT: hello Mario

greeting(language='it', default='hi', name='Mario') #passing keyword arguments
# One of the benefits of using keyword arguments is that we can actually put this in
# any order we please,
#OUTPUT: hello Mario

# greeting(language='it', default='hi')
#Trimmed Output: TypeError: greeting() missing 1 required positional argument: 'name'

# greeting(language='it', default='hi','Mario')
# SyntaxError: positional argument follows keyword argument

# greeting('Mario', default='hi')
# TypeError: greeting() missing 1 required positional argument: 'language'

# greeting('Mario', language='cs')
# TypeError: greeting() missing 1 required positional argument: 'default'


def greeting1(name: str = None, language: str = None, default: str = None):
    if language == 'it':
        print(f'hello {name}')
    else:
        print(f'{default} {name}')


greeting1()
# None None

greeting1('Mario','it','hello')
# hello Mario

greeting1(default='Howdy')
# Howdy None
