def is_strong_password(password: str) -> bool:
    """
    Sprawdza, czy hasło spełnia warunki silnego hasła:
    - co najmniej 8 znaków
    - przynajmniej jedna duża litera
    - przynajmniej jedna mała litera
    - przynajmniej jedna cyfra
    - przynajmniej jeden znak specjalny (!@#$%^&*())
    """
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*()" for c in password)
    )
