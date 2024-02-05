import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hw.hw_34.hw_34 import add_user, get_user_by_id, get_all_users, update_user, delete_user_by_id, User, Base


@pytest.fixture
def setup_database():
    engine = create_engine('sqlite:///:memory:', echo=True, future=True)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    session = SessionLocal()
    yield session
    session.close()


# Функция для добавления начальных пользователей в базу данных
def add_initial_users(session):
    user_data_list = [
        {"FirstName": "Test1", "LastName": "User1", "Password": "password1", "Email": "testuser1@example.com",
         "VKID": "testuser123"},
        {"FirstName": "Test2", "LastName": "User2", "Password": "password2", "Email": "testuser2@example.com",
         "VKID": None},
        {"FirstName": "Test3", "LastName": "User3", "Password": None, "Email": "testuser3@example.com",
         "VKID": "testuser456"}
    ]
    for user_data in user_data_list:
        add_user(session, user_data)


@pytest.mark.parametrize("user_data", [
    {"FirstName": "Test1", "LastName": "User1", "Password": "password1", "Email": "testuser1@example.com",
     "VKID": "testuser123"},
    {"FirstName": "Test2", "LastName": "User2", "Password": "password2", "Email": "testuser2@example.com",
     "VKID": None},
    {"FirstName": "Test3", "LastName": "User3", "Password": None, "Email": "testuser3@example.com",
     "VKID": "testuser456"},
])
def test_add_user(setup_database, user_data):
    session = setup_database
    user_id = add_user(session, user_data)
    assert user_id is not None


def test_get_user_by_id(setup_database):
    session = setup_database
    add_initial_users(session)
    user = get_user_by_id(session, 1)
    assert user is not None
    assert user['FirstName'] == "Test1"


def test_get_all_users(setup_database):
    session = setup_database
    add_initial_users(session)
    users = get_all_users(session)
    assert len(users) == 3


@pytest.mark.parametrize("user_id, update_data, expected_firstname", [
    (1, {"FirstName": "Updated1", "LastName": "User1", "Password": "password1", "Email": "testuser1@example.com",
         "VKID": "testuser123"}, "Updated1"),
    (2, {"FirstName": "Updated2", "LastName": "User2", "Password": "password2", "Email": "testuser2@example.com",
         "VKID": None}, "Updated2"),
    (3, {"FirstName": "Updated3", "LastName": "User3", "Password": None, "Email": "testuser3@example.com",
         "VKID": "testuser456"}, "Updated3"),
])
def test_update_user(setup_database, user_id, update_data, expected_firstname):
    session = setup_database
    add_initial_users(session)
    update_user(session, {"UserID": user_id, **update_data})
    updated_user = get_user_by_id(session, user_id)
    assert updated_user['FirstName'] == expected_firstname


@pytest.mark.parametrize("user_id_to_delete", [1, 2, 3])
def test_delete_user_by_id(setup_database, user_id_to_delete):
    session = setup_database
    add_initial_users(session)
    delete_user_by_id(session, user_id_to_delete)
    user = get_user_by_id(session, user_id_to_delete)
    assert user is None
