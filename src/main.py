def hello():
 feature/header-design-a
    print("Hello user, its me, version A and B!")   
 main
def goodbye():
    print("Goodbye user!")

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
