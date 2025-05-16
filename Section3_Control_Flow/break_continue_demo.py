number: int = 5
while number > 0:
    number -= 1

    if number == 2:
        print('Break at 2')
        break

    print(number)

print('Done!')


number: int = 5
while number > 0:
    number -= 1

    if number == 2:
        print('Skipping at 2')
        continue

    print(number)

print('Done!')

total: int = 0
print('Welcome to Calc+! Add positive numbers, or enter 0 to exit')
while True:
    user_input: int = int(input('Enter a number: '))

    if user_input < 0:
        print('!!!Please enter positive numbers only!!!')
        continue

    if user_input == 0:
        print(f'Total: {total}')
        break

    total += user_input