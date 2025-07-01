def hello():
    print("Hellow world!")
def goodbye():
    print("Goodbye world!")

def show_menu():
    print("=== MENU APLIKACJI ===")
    print("1. Start")
    print("2. Pomoc")
    print("3. Wyjście")

def main():
    show_menu()
    choice = input("Wybierz opcję: ")
    print(f"Wybrałeś opcję: {choice}")

if __name__ == "__main__":
    main()

