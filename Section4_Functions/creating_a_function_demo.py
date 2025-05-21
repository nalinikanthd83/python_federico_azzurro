import time


def greet():
    print('Hello')
    print('------')

greet()
greet()
greet()
# Hello
# ------
# Hello
# ------
# Hello
# ------

from datetime import datetime

def show_time():
    now: datetime = datetime.now()
    print(f'Time: {now:%H:%M:%S}')

show_time()
time.sleep(5)
show_time()
# Time: 14:42:10
# Time: 14:42:15
