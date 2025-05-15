a: float = 200.312399
b: float = 18.12132
c: float = 47.12312

result: float = a + b + c
print(result)  #OUTPUT: 265.55683899999997

rounded: float = round(result, 2)
print(rounded)  #OUTPUT: 265.56
print(round(result, 2))  #OUTPUT: 265.56
print(round(result, 1))  # 265.6
print(round(result, 0))  # 266.0
print(round(result, -1))  # 270.0
print(round(result, -2))  # 300.0
