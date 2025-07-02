def hello():
 feature/header-design-a
    print("Hello user, its me, version A and B!")   
 main
def goodbye():
    print("Goodbye user!")

def start_app():
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
# nowa opcja dodana w celu zadania z lab2
def show_menu():
    print("1. Start")
    print("2. Pomoc")
    print("3. Wyjście")
    print("4. Informacje")  

def start_app():
    show_menu()
    choice = input("Wybierz opcję: ")
    if choice == "4":
        print("To aplikacja stworzona przez Adrian 💡")

     
