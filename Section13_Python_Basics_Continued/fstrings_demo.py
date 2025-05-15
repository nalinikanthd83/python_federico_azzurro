var: int = 10

def add(a: int, b: int) -> int:
    return a + b

print(f'{var=}') #OUTPUT: var=10

# And when we run this what you're going to notice in the console is the variable name plus its value.
# And that's ultra convenient because that just saves us the trouble from having to write out var equals
# var.

print(f'{add(5, 10) = }') #OUTPUT: add(5, 10) = 15

big_number: float = 123456789
print(f'{big_number:,}') #OUTPUT: 123,456,789
# comma is going to work as the thousand separator

print(f'{big_number:_}') #OUTPUT: 123_456_789
# in this example, _ is going to work as the thousand separator


big_number: float = 123_45_6_7_8_9
print(big_number) #OUTPUT: 123456789

# At any point when you're creating a number in Python, you
# can use the underscore anywhere in your number and Python will ignore it.
# And the reason you would do this is to make your numbers more legible
# when you are creating them

fraction: float = 1234.5678
print(f'{fraction:.2f}') #OUTPUT: 1234.57
# going to round it to two decimal places as a float

print(f'{fraction:_.2f}') #OUTPUT: 1_234.57
print(f'{fraction:,.2f}') #OUTPUT: 1,234.57

percent: float = 0.5
print(f'{percent:.2%}') #OUTPUT: 50.00%
print(f'{percent:.0%}') #OUTPUT: 50%

percent: float = 0.55555555
print(f'{percent:.3%}') #OUTPUT: 55.556%


percent: float = 55.55555555
print(f'{percent:,.3%}') #OUTPUT: 5,555.556%
print(f'{percent:_.3%}') #OUTPUT: 5_555.556%

var: str = 'BOB'
print(f'{var:10}: Hello')                   #OUTPUT: BOB       : Hello
print(f'{var:>10}: Hello')  #Right aligned  #OUTPUT:        BOB: Hello
print(f'{var:<10}: Hello')  #Left aligned   #OUTPUT: BOB       : Hello
print(f'{var:^10}: Hello')  #Center aligned #OUTPUT:    BOB    : Hello

var: str = 'BOB'
print(f'{var:.>10}') #Right aligned  #OUTPUT: .......BOB
print(f'{var:.<10}') #Left aligned   #OUTPUT: BOB.......
print(f'{var:.^10}') #Center aligned #OUTPUT: ...BOB....

# Any symbol can be used not just .

var: str = 'BOB'
print(f'{var:#>10}') #Right aligned  #OUTPUT: #######BOB
print(f'{var:$<10}') #Left aligned   #OUTPUT: BOB$$$$$$$
print(f'{var:@^10}') #Center aligned #OUTPUT: @@@BOB@@@@

numbers: list[int] = [1, 100, 1_000, 10_000]
for number in numbers:
    print(f'{number:_>5}: counting!')

#OUTPUT
# ____1: counting!
# __100: counting!
# _1000: counting!
# 10000: counting!

numbers: list[int] = [1, 100, 1_000, 10_000]
for number in numbers:
    print(f'{number:>5}: counting!')

#OUTPUT
#     1: counting!
#   100: counting!
#  1000: counting!
# 10000: counting!

asterisk: str = '*'
for i in range(1,6):
    print(f'{asterisk:>{i}}')

#OUTPUT
# *
#  *
#   *
#    *
#     *

path: str = '\\Users\\guest\\docs\\'
print(path) #OUTPUT: \Users\guest\docs\

path: str = r'\Users\guest\docs'
print(path) #OUTPUT: \Users\guest\docs\

user: str = 'guest'
path: str = fr'\Users\{user}\docs'
print(path) #OUTPUT: \Users\guest\docs\
path: str = rf'\Users\{user}\docs'
print(path) #OUTPUT: \Users\guest\docs\

# can use rf or fr