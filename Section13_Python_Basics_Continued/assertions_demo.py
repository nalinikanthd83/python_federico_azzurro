def start_program(db: dict[int, str]) -> None:
    assert db, 'Database is empty'

    print('Loaded:', db)
    print('Program started successfully!')

def main() -> None:
    db1: dict[int, str] = {0: 'a', 1: 'b'}
    db2: dict[int, str] = {}
    start_program(db2)
    # Trimmed Output: AssertionError: Database is empty

if __name__ == '__main__':
    ...
    #main() //Uncomment and run the program

var: int = -5
assert var > 0, f'{var} is not greater than 0'
# Trimmed Output: AssertionError: -5 is not greater than 0