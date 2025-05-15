numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ['A', 'B', 'C', 'D']
symbols: list[str] = ['!', '$', '#']

zipped: zip = zip(numbers, letters)
print(zipped) #OUTPUT: <zip object at 0x000002892491BFC0>
print(list(zipped)) #OUTPUT: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]

zipped: zip = zip(numbers, letters)
for n,l in zipped:
    print(n, l, sep=': ')

#OUTPUT
# 1: A
# 2: B
# 3: C
# 4: D

zipped: zip = zip(numbers, symbols)
for n,s in zipped:
    print(n, s, sep=': ')

#OUTPUT
# 1: !
# 2: $
# 3: #

zipped: zip = zip(numbers, symbols, letters)
print(list(zipped)) #OUTPUT: [(1, '!', 'A'), (2, '$', 'B'), (3, '#', 'C')]

zipped: zip = zip(numbers, symbols, strict=True)
for n,s in zipped:
    print(n, s, sep=': ')

# OUTPUT
# Traceback (most recent call last):
#   File "C:\Users\nalin\PycharmProjects\Python_Federico_Azzurro\Section12_Builtin_Functions\zip_demo.py", line 24, in <module>
#     for n,s in zipped:
#                ^^^^^^
# ValueError: zip() argument 2 is shorter than argument 1





