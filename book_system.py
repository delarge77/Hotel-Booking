from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer
import uuid
from datetime import datetime


# ============================================================
# INITIAL DATA
# ============================================================

customers_data = [
    {
        "id_customer": "34324234",
        "name": "Alessandro",
        "age": 25
    },
    {
        "id_customer": "customer002",
        "name": "John",
        "age": 34
    },
    {
        "id_customer": "customer003",
        "name": "Maria",
        "age": 29
    }
]

rooms_data = [
    {
        "id_room": "idroom001",
        "number": "123",
        "is_available": False
    },
    {
        "id_room": "idroom002",
        "number": "124",
        "is_available": True
    },
    {
        "id_room": "idroom003",
        "number": "125",
        "is_available": True
    },
    {
        "id_room": "idroom004",
        "number": "126",
        "is_available": True
    },
    {
        "id_room": "idroom005",
        "number": "127",
        "is_available": True
    }
]

hotels_data = [
    {
        "id_hotel": "3423423",
        "address": "körsbärsgatan 5A",
        "rooms": ["idroom001", "idroom002", "idroom003"]
    },
    {
        "id_hotel": "hotel002",
        "address": "Avenyn 10, Göteborg",
        "rooms": ["idroom004", "idroom005"]
    }
]

bookings_data = [
    {
        "hotel": "3423423",
        "room": "idroom001",
        "customer": "34324234",
        "start_date": "2026-10-01",
        "end_date": "2026-10-05",
        "price": 320.00
    }
]

# ============================================================
# CREATE ROOMS
# ============================================================

rooms = []
for room_data in rooms_data:
    room = Room(
        room_data["id_room"],
        room_data["number"],
        room_data["is_available"]
    )
    rooms.append(room)

# ============================================================
# CREATE HOTELS
# ============================================================

hotels = []
for hotel_data in hotels_data:
    hotel_rooms = [room for room in rooms if room.id_room in hotel_data["rooms"]]
    hotel = Hotel(
        hotel_data["id_hotel"],
        hotel_data["address"],
        hotel_rooms
    )
    hotels.append(hotel)

# ============================================================
# CREATE CUSTOMERS
# ============================================================

customers = []
for customer_data in customers_data:
    customer = Customer(
        customer_data["id_customer"],
        customer_data["name"],
        customer_data["age"]
    )
    customers.append(customer)

# ============================================================
# CREATE INITIAL BOOKINGS
# ============================================================

bookings = []
for booking_data in bookings_data:
    customer = next((customer for customer in customers if customer.id_customer == booking_data["customer"]), None)
    room = next((room for room in rooms if room.id_room == booking_data["room"]), None)
    hotel = next((hotel for hotel in hotels if hotel.id_hotel == booking_data["hotel"]), None)

    if customer is not None and room is not None and hotel is not None:
        booking = Booking(
            hotel,
            room,
            customer,
            booking_data["start_date"],
            booking_data["end_date"],
            booking_data["price"]
        )

        # The room is already marked as unavailable
        # because this booking already exists.
        room.is_available = False

        # Add the booking to the hotel and global list.
        hotel.bookings.append(booking)
        bookings.append(booking)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_age():
    while True:
        try:
            age = int(input("Type customer age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            return age

        except ValueError:
            print("Please enter a valid age.")


def get_date(message):
    while True:
        date_input = input(message)
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


# ============================================================
# SHOW HOTELS
# ============================================================

def show_hotels():

    print("=============================")
    print("           HOTELS             ")
    print("=============================")

    for hotel in hotels:
        print(hotel)

    input("Press any key to continue ... ")


# ============================================================
# SHOW AVAILABLE ROOMS
# ============================================================

def show_available_rooms():

    print("=============================")
    print("      AVAILABLE ROOMS        ")
    print("=============================")

    for hotel in hotels:

        print(f"\nHotel: {hotel.id_hotel}")

        available_rooms = hotel.checkAvailability()

        if len(available_rooms) == 0:
            print("No rooms available.")
        else:
            for room in available_rooms:
                print(f"Room: {room.number}")

    input("\nPress any key to continue ... ")


# ============================================================
# SHOW CUSTOMERS
# ============================================================

def show_all_customers():

    print("=============================")
    print("          CUSTOMERS           ")
    print("=============================")

    if len(customers) == 0:
        print("There are no customers.")

    else:
        for customer in customers:
            print(customer)

    input("\nPress any key to continue ... ")


# ============================================================
# REGISTER CUSTOMER
# ============================================================

def register_customer():

    print("=============================")
    print("       ADD CUSTOMER           ")
    print("=============================")

    id_customer = str(uuid.uuid4())

    name = input("Type customer name: ")

    while name.strip() == "":
        print("Name cannot be empty.")
        name = input("Type customer name: ")

    age = get_age()

    new_customer = Customer(
        id_customer,
        name,
        age
    )

    customers.append(new_customer)

    print("\nCustomer added successfully!")
    print(new_customer)

    input("\nPress any key to continue ... ")


# ============================================================
# SHOW BOOKINGS
# ============================================================

def show_all_bookings():

    print("=============================")
    print("          BOOKINGS             ")
    print("=============================")

    if len(bookings) == 0:
        print("There are no bookings at the moment.")

    else:
        for booking in bookings:
            print(
            f"Hotel: {booking.hotel} | "f"Room number: {booking.room.number} "
            f"Customer name: {booking.customer.name} | "f"Start date: {booking.start_date} "
            f"End date: {booking.end_date}"
            )

    input("\nPress any key to continue ... ")


# ============================================================
# CREATE BOOKING - CHOOSE HOTEL
# ============================================================

def show_create_booking():

    print("=============================")
    print("       CHOOSE A HOTEL         ")
    print("=============================")

    for hotel in hotels:
        print(
            f"ID: {hotel.id_hotel} | "
            f"Address: {hotel.address}"
        )

    selected_hotel_id = input("\nHotel ID: ")

    selected_hotel = next((hotel for hotel in hotels if hotel.id_hotel == selected_hotel_id), None )

    if selected_hotel is None:
        print("Hotel not found.")
        input("Press any key to continue ... ")
        return

    show_available_rooms_menu(selected_hotel)


# ============================================================
# CREATE BOOKING - CHOOSE ROOM
# ============================================================

def show_available_rooms_menu(selected_hotel):

    print("=============================")
    print("      AVAILABLE ROOMS        ")
    print("=============================")

    available_rooms = selected_hotel.checkAvailability()

    if len(available_rooms) == 0:
        print("There are no available rooms in this hotel.")
        input("Press any key to continue ... ")
        return

    for room in available_rooms:
        print(f"Room: {room.number}")

    while True:
        room_number = input("\nChoose room number: ")
        selected_room = next((room for room in available_rooms if room.number == room_number), None)
        if selected_room is not None:
            show_customers(selected_hotel, selected_room)
            break

        print("Please choose a valid room.")


# ============================================================
# CREATE BOOKING - CHOOSE CUSTOMER
# ============================================================

def show_customers(selected_hotel, selected_room):

    print("=============================")
    print("       CHOOSE CUSTOMER        ")
    print("=============================")

    for customer in customers:
        print(
            f"ID: {customer.id_customer} | "
            f"Name: {customer.name}"
        )

    while True:
        customer_id = input("\nSelect customer ID: ")
        selected_customer = next((customer for customer in customers if customer.id_customer == customer_id), None)
        if selected_customer is not None:
            selected_dates(selected_hotel, selected_room, selected_customer)
            break
        print("Customer not found. Please try again.")

# ============================================================
# CREATE BOOKING - SELECT DATES
# ============================================================

def selected_dates(selected_hotel, selected_room, selected_customer):
    print("=============================")
    print("       SELECT START DATE      ")
    print("=============================")

    start_date = get_date("Start date (YYYY-MM-DD): ")

    print("=============================")
    print("        SELECT END DATE       ")
    print("=============================")

    end_date = get_date("End date (YYYY-MM-DD): ")

    # Make sure the end date is after the start date.
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if end <= start:
        print("\nEnd date must be after start date.")
        input("Press any key to continue ... ")
        return

    new_booking = Booking(selected_hotel, selected_room, selected_customer, start_date, end_date)
    confirm_new_booking(new_booking)

# ============================================================
# CONFIRM BOOKING
# ============================================================

def confirm_new_booking(new_booking):

    print("=============================")
    print("       CONFIRM BOOKING        ")
    print("=============================")

    print(f"Hotel: {new_booking.hotel.id_hotel}")
    print(f"Room: {new_booking.room.number}")
    print(f"Customer: {new_booking.customer.name}")
    print(f"Start date: {new_booking.start_date}")
    print(f"End date: {new_booking.end_date}")

    confirm = input("\nConfirm booking? Y / N: ")

    if confirm.lower() == "y":
        # Save booking in the hotel.
        new_booking.hotel.saveBooking(new_booking)

        # Add the same booking to the global booking list.
        bookings.append(new_booking)

        print("=============================")
        print("       BOOKING CONFIRMED      ")
        print("=============================")

        print("Booking confirmed with ID:", new_booking.id_booking)
    else:
        print("\nBooking cancelled.")

    input("\nPress any key to continue ... ")


# ============================================================
# CANCEL BOOKING
# ============================================================

def cancel_booking():
    print("=============================")
    print("       CANCEL BOOKING         ")
    print("=============================")

    for book in bookings:
        print(
            f"ID: {book.id_booking} | "
            f"Customer: {book.customer.name} | "
            f"Room: {book.room.number}"
        )

    id_booking = input("\nType booking ID: ")

    selected_booking = next((book for book in bookings if book.id_booking == id_booking), None)

    if selected_booking is None:
        print("Booking does not exist.")
        input("Press any key to continue ... ")
        return

    print("\nBooking found:")
    print(selected_booking)

    confirm = input("\nConfirm cancelling booking? Y / N: ")

    if confirm.lower() == "y":
        # Cancel booking inside the hotel.
        selected_booking.hotel.cancelBooking(selected_booking.id_booking)

        # Remove the booking from the global list.
        if selected_booking in bookings:
            bookings.remove(selected_booking)

        print("=============================")
        print("       BOOKING CANCELLED     ")
        print("=============================")

        print("Booking cancelled successfully.")
    else:
        print("Cancellation aborted.")

    input("\nPress any key to continue ... ")


# ============================================================
# MAIN MENU
# ============================================================

option = 0
while option != 8:
    print("=============================")
    print("     HOTEL BOOKING SYSTEM    ")
    print("=============================")
    print("1. Show hotels")
    print("2. Show available rooms")
    print("3. Show customers")
    print("4. Add new customer")
    print("5. Show bookings")
    print("6. Make a booking")
    print("7. Cancel a booking")
    print("8. Exit")

    try:
        option = int(input("\nChoose an option: "))
    except ValueError:
        print("\nPlease type a number from 1 to 8.")
        continue

    if option == 1:
        show_hotels()
    elif option == 2:
        show_available_rooms()
    elif option == 3:
        show_all_customers()
    elif option == 4:
        register_customer()
    elif option == 5:
        show_all_bookings()
    elif option == 6:
        show_create_booking()
    elif option == 7:
        if len(bookings) > 0:
            cancel_booking()
        else:
            print("\nThere are no bookings at the moment.")
            input("Press any key to continue ... ")
    elif option == 8:
        print("\nThank you for using the Hotel Booking System!")
    else:
        print("\nPlease type a valid option.")