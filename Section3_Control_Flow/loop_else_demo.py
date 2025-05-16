
for i in range(3):
    print(f'Iteration: {i}')
else:
    print('Success!')  #this else block gets executed only when the loop terminates normally
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Success!


for i in range(3):
    print(f'Iteration: {i}')
    break
else:
    print('Success!') #this else block will not get executed because loop
    # is terminating because of break
# Iteration: 0

i: int = 3

while i > 0:
    i -= 1
    print('OK')
else:
    print('Success!')
# OK
# OK
# OK
# Success!

i: int = 3

while i > 0:
    i -= 1
    print('OK')
    break
else:
    print('Success!')
# OK
