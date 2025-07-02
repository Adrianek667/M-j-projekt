from password_validator import is_valid_password

def test_password_flow():
    cases = {
        "Test1234": True,
        "12345678": False,
        "test": False,
        "TESTTEST": False,
        "TestTest": False,
        "": False
    }
    for pwd, expected in cases.items():
        assert is_valid_password(pwd) == expected
