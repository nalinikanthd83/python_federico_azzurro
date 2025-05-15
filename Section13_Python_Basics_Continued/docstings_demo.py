class User:
    """
    Base class for creating users.
    """

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def show_id(self):
        """Returns user id as an int"""
        print(self.user_id)

def user_exists(user: User, database: set[User]) -> bool:
    """
    below text is auto-generated when docstrings are added
    This is Sphnix Markup
    Read more at: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html

    :param user:
    :param database:
    :return:
    """
    return user in database

def main() -> None:

    bob: User = User(0)
    anna: User = User(1)

    database: set[User] = {bob, anna}

    if user_exists(bob, database):
        print('User is found in database!')
    else:
        print('User is not found in database')

    print(User.__doc__)
    print(user_exists.__doc__)

if __name__ == '__main__':
    main()