
def get_length(text: str) -> int:
    return len(text)

name: str = 'Mario'
length: int = get_length(name)
print(length) #OUTPUT: 5

# print(len(10))
# TypeError: object of type 'int' has no len()

def make_upper(text: str) -> str:
    return text.upper()

print(make_upper('hello')) #HELLO


def connect_to_internet() -> None:
    print('Connecting to internet....')

var: str = connect_to_internet()
# Expected str but got None

print(connect_to_internet())
# Connecting to internet....
# None