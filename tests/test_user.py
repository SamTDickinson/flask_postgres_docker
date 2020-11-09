from application.models import User


def test_create_user(database):
    email = "some.email@server.com"
    password = "test_password"
    salt = "banana"
    user = User(email=email, password=password, salt=salt)
    database.session.add(user)
    database.session.commit()

    user = User.query.first()

    assert user.email == email
    assert user.salt == "banana"
    assert user.password == "test_password"