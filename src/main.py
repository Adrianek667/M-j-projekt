def hello():
    print("Hello world!")
def goodbye():
    print("Goodbye world!")

def main():
    show_menu()
    choice = input("Wybierz opcję: ")

    if choice == "1":
        hello()
    elif choice == "2":
        print("To jest przykładowa pomoc 🆘")
    elif choice == "3":
        goodbye()
    else:
        print("Nieznana opcja.")
