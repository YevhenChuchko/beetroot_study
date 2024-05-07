from Air_utils import show_apartments, choice_apartment

while True:
    print("Welcome to the Air Apartment!")
    message = ("""
                    To book an apartment, follow these steps: 
                    1. Show all apartments
                    2. Choose an apartment
                       Select the booking dates 
                       Enter your first and last name
                    0. Exit 

                    Your Choice: """)

    choice = input(message)
    match choice:
        case "1":
            show_apartments()
        case "2":
            choice_apartment()
        case "0":
            break
        case _:
            print("Wrong choice, try again")