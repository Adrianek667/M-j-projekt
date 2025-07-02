def hello():
    print("Witaj użytkowniku 👋")

def goodbye():
    print("Do zobaczenia! 👋")

def show_menu():
    print("\n--- MENU ---")
    print("1. Przywitaj się")
    print("2. Pomoc")
    print("3. Wyjście")
    print("4. Informacje")

def start_app():
    show_menu()
    choice = input("Wybierz opcję: ")

    if choice == "1":
        hello()
    elif choice == "2":
        print("To jest przykładowa pomoc 🆘")
    elif choice == "3":
        goodbye()
    elif choice == "4":
        print("To aplikacja stworzona przez Adriana 👨‍💻")
    else:
        print("Nieznana opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    start_app()

