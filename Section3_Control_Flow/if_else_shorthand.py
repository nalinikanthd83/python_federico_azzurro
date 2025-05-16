a: int = 10
b: int = 35
c: int = 50

biggest_number: int = a if a > b and a > c else b if b > c else c

print(biggest_number)