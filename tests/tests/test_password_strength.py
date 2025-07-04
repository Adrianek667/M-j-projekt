from src.password_strength import is_strong_password


def test_strong_password():
    assert is_strong_password("Test1234!") is True


def test_weak_password_no_special():
    assert is_strong_password("Test1234") is False
