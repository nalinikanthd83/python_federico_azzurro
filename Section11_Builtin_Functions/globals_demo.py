# globals() - This tells us exactly what is visible inside the global namespace

from typing import Any

text: str = 'Bob'
my_list: list[int] = [1, 2, 3]

def main() -> None:
    ...

print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001EEA543C4B0>, '__spec__': None, '__annotations__': {'text': <class 'str'>, 'my_list': list[int]}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\nalin\\PycharmProjects\\Python_Federico_Azzurro\\Section11_Builtin_Functions\\globals_demo.py', '__cached__': None, 'Any': typing.Any, 'text': 'Bob', 'my_list': [1, 2, 3], 'main': <function main at 0x000001EEA54939C0>}

# So this is returning everything that is visible in the global scope,
# which is the outermost layer of our script.

my_globals: dict[str, Any] = dict(globals())

for k,v in my_globals.items():
    print(f'{k}:{v}')

# __name__:__main__
# __doc__:None
# __package__:None
# __loader__:<_frozen_importlib_external.SourceFileLoader object at 0x0000021C0003C4B0>
# __spec__:None
# __annotations__:{'text': <class 'str'>, 'my_list': list[int], 'my_globals': dict[str, typing.Any]}
# __builtins__:<module 'builtins' (built-in)>
# __file__:C:\Users\nalin\PycharmProjects\Python_Federico_Azzurro\Section11_Builtin_Functions\globals_demo.py
# __cached__:None
# Any:typing.Any
# text:Bob
# my_list:[1, 2, 3]
# main:<function main at 0x0000021C7FDB1440>




