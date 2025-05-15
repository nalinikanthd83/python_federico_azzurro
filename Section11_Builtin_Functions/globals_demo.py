# globals function - This tells us exactly what is visible inside the
# global namespace

from typing import Any

print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D083E1C4B0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\nalin\\PycharmProjects\\Python_Federico_Azzurro\\Section11_Builtin_Functions\\globals_demo.py', '__cached__': None, 'Any': typing.Any}

# So this is returning everything that is visible in the global scope,
# which is the outermost layer of our script.


