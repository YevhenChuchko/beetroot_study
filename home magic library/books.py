from utils import list_of_all_books, add_new_book

def show_main_menu():
    while True:
        print("""Main menu:\n  1 - View a list of all books\n  2 - Add a new book\n  0 - Sing out""")
        user_choice = input("Make your choice: ")
        if user_choice == "1":
            list_of_all_books()
        elif user_choice == '2':
            add_new_book()
        elif user_choice == '0':
            print("You have logged out. See you soon!")
            break
        else:
            print("Incorrect input, select a digit from the main menu list")


show_main_menu()