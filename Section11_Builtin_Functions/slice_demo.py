numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers[2:4])  # [3, 4]

text: str = 'Hello, world!'
first_three: slice = slice(0, 3)
# creating a reusable slice object

print(text[first_three]) # Hel
print(text[0:3]) # Hel

reverse_slice = slice(None, None, -1)
print(text[reverse_slice]) # !dlrow ,olleH

text: str = 'Hello  world!'
step_two = slice(None, None, 2)
print(text[step_two]) # Hlo ol!
print('Second Text'[step_two]) # Scn et

