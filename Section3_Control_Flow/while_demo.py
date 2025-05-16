import time

connected: bool = True

while connected:
    print('connected...')
    time.sleep(5)
    connected = False

print('Not connected...')

while True:
    user_input: str = input('You: ')

    if user_input == 'hello':
        print('Bot: Hey there!')
    else:
        print('Bot: Yes, that is interesting!')
