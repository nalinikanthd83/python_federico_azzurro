text: str = 'Hello World'

for i in range(3):
    print(f'{i+1}: {text}')
# 1: Hello World
# 2: Hello World
# 3: Hello World

peoples: list[str] = ['Bob', 'James', 'Maria']

for person in peoples:
    if len(person) > 4:
        print(f'{person} has long name')
    else:
        print(f'{person} has short name')



