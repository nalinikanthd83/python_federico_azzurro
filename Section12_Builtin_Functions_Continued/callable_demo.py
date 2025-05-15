# callable() - It allows us to check whether an object is callable or not.

fruit: str = 'apple'
number: int = 10

def func() -> None:
    print('func() was called')



print(f'callable {callable(fruit)}')  # OUTPUT: callable False
print(f'callable {callable(number)}') # OUTPUT: callable False
print(f'callable {callable(func)}')   # OUTPUT: callable True
print(f'callable {callable(range)}')   # OUTPUT: callable True
print(f'callable {callable(str)}')   # OUTPUT: callable True


if callable(func):
    func() #OUTPUT: func() was called
else:
    print(f'func is not callable')


fruit()
 # Traceback (most recent call last):
 # File "C:\Users\nalin\PycharmProjects\Python_Federico_Azzurro\Section13\callable_demo.py", line 13, in <module>
 #   fruit()
 #   ~~~~~^^
# TypeError: 'str' object is not callable

