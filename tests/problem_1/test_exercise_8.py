from src.problem_1.exercise_8 import User


def test_get_total_users_with_no_users(setup_users_database):
    """
    Test exercise_8.User the initial total number of users when no users are created.
    GIVEN an empty database,
    WHEN querying the total number of users,
    THEN the returned value should be 0.
    """
    assert User.get_total_users() == 0


def test_get_total_users_with_one_user(setup_users_database):
    """
    Test exercise_8.User the initial total number of users when one user is created.
    GIVEN an empty database,
    WHEN creating one user and querying the total number of users,
    THEN the returned value should be 1.
    """
    User("User1", "password1")
    assert User.get_total_users() == 1


def test_get_total_users_with_multiple_users(setup_users_database):
    """
    Test exercise_8.User the initial total number of users when some users are created.
    GIVEN an empty database,
    WHEN creating three users and querying the total number of users,
    THEN the returned value should be 3.
    """
    User("User1", "password1")
    User("User2", "password2")
    User("User3", "password3")
    assert User.get_total_users() == 3
