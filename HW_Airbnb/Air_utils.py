class Rental:
    def __init__(self, guests_count, beds_count, rooms_count, apartment_grade):
        self.guests_count = guests_count
        self.beds_count = beds_count
        self.rooms_count = rooms_count
        self.apartment_grade = apartment_grade
        self.reservations = []

    def is_available(self, start_date, end_date):
        for reservation in self.reservations:
            if start_date < reservation["end_date"] and end_date > reservation["start_date"]:
                return False
        return True

    def reserve(self, start_date, end_date, guest_last_name, guest_first_name):
        if self.is_available(start_date, end_date):
            self.reservations.append({
                "start_date": start_date,
                "end_date": end_date,
                "guest_last_name": guest_last_name,
                "guest_first_name": guest_first_name
            })
            print("Reservation successful!")
        else:
            print("Sorry, the apartment is not available for the selected dates.")


class Booking:
    def __init__(self, start_date, end_date, guest_last_name, guest_first_name, rental):
        self.start_date = start_date
        self.end_date = end_date
        self.guest_last_name = guest_last_name
        self.guest_first_name = guest_first_name
        self.rental = rental


apartment1 = Rental(2, 2, 2, "Standard")
apartment2 = Rental(2, 1, 1, "Economy")
apartment3 = Rental(1, 1, 1, "Lux")


def choice_apartment():
    klient_choice = input("Please, enter the apartment number (1, 2, 3):  ")
    if klient_choice == "1":
        make_reservation(apartment1)
    elif klient_choice == "2":
        make_reservation(apartment2)
    elif klient_choice == "3":
        make_reservation(apartment3)
    else:
        print("Wrong choise, try again")


def make_reservation(rental):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    guest_last_name = input("Enter your last name: ")
    guest_first_name = input("Enter your first name: ")
    rental.reserve(start_date, end_date, guest_last_name, guest_first_name)


def show_apartments():
    print("Apartment 1:")
    print(f"Guests Count: {apartment1.guests_count}")
    print(f"Beds Count: {apartment1.beds_count}")
    print(f"Rooms Count: {apartment1.rooms_count}")
    print(f"Apartment Grade: {apartment1.apartment_grade}\n")

    print("Apartment 2:")
    print(f"Guests Count: {apartment2.guests_count}")
    print(f"Beds Count: {apartment2.beds_count}")
    print(f"Rooms Count: {apartment2.rooms_count}")
    print(f"Apartment Grade: {apartment2.apartment_grade}\n")

    print("Apartment 3:")
    print(f"Guests Count: {apartment3.guests_count}")
    print(f"Beds Count: {apartment3.beds_count}")
    print(f"Rooms Count: {apartment3.rooms_count}")
    print(f"Apartment Grade: {apartment3.apartment_grade}")
