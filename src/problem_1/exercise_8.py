class User:
    """
    Represents a user in the database.
    """

    _total_users = 0

    def __init__(self, name: str, password: str):
        """
        Initializes a new User instance.
        :param name: The name of the user.
        :param password: The password of the user.
        """
        self.name = name
        self.password = password
        User._total_users += 1

    @staticmethod
    def get_total_users() -> int:
        """
        Returns the total number of users already created
        """
        return User._total_users
