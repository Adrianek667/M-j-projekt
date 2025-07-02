from password_validator import is_valid_password

def test_valid_password():
    assert is_valid_password("Test1234") is True

def test_too_short():
    assert is_valid_password("T1a") is False

def test_missing_uppercase():
    assert is_valid_password("test1234") is False

def test_missing_lowercase():
    assert is_valid_password("TEST1234") is False

def test_missing_digit():
    assert is_valid_password("TestTest") is False
