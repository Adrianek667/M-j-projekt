import os


def goodbye():
    print("\n👋 Dzięki za skorzystanie z aplikacji!\n")


def emergency_help():
    print("\n🆘 Funkcja pomocy awaryjnej jest jeszcze w budowie...\n")


def developer_info():
    print("\n🧑‍💻 Autor: Adrian | Projekt Railway CI/CD\n")


def password_strength_check():
    print("\n🔒 Sprawdzanie siły hasła...\n")
    # Tutaj może być logika z password_validator


def main_menu():
    print("\n=== MENU GŁÓWNE ===")
    print("1. Informacje o programie")
    print("2. Sprawdź hasło")
    print("3. Pomoc awaryjna")
    print("4. Wyjście")

    choice = input("Wybierz opcję (1-4): ")

    if choice == "1":
        developer_info()
    elif choice == "2":
        password_strength_check()
    elif choice == "3":
        emergency_help()
    elif choice == "4":
        goodbye()
    else:
        print("\n⚠️ Niepoprawna opcja. Spróbuj ponownie.\n")


if __name__ == "__main__":
    while True:
        main_menu()
