
def func() -> None:
    print('Recursion')
    func()

# func()
# RecursionError: maximum recursion depth exceeded
# function gets called recursively and that's why the error
# our computers usually implement a safety mechanism that prevents it from running forever,

import time

def connect_to_internet(signal: bool, delay: int) -> None:
    if delay > 5:
        signal = True

    if signal:
        print('Connected....')
    else:
        print(f'Connection failed. Try again in {delay} seconds')
        time.sleep(delay)
        connect_to_internet(signal, delay + 2)

connect_to_internet(False, 0)

# Connection failed. Try again in 0 seconds
# Connection failed. Try again in 2 seconds
# Connection failed. Try again in 4 seconds
# Connected....

import sys
def my_factorial(number: int) -> int:
    if number < 0:
        print('Enter only positive number')
        sys.exit()

    if number == 0 or number == 1:
        return 1
    else:
        return number * my_factorial(number - 1)

print(my_factorial(2))
#print(my_factorial(-2))
print(my_factorial(5))

