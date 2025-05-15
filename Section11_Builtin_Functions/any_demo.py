# any() checks that at least one element in a list or an iterable is true for
# it to pass the check

people_voted: list[int] = [0, 1, 0, 0, 0, 0, 0]

if any(people_voted):
    print('At least one person voted')
else:
    print('No one voted')
#OUTPUT: At least one person voted


if any([0, 1, 0, 0, 0, 0, 0]): #Passing list directly instead of variable
    print('At least one person voted')
else:
    print('No one voted')
#OUTPUT: At least one person voted