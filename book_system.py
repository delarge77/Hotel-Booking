from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer
import uuid

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
        "id_room": "eqwewe",
        "number": "123",
        "is_available": False
    },
    {
        "id_room": "sdadasdsa",
        "number": "124",
        "is_available": True
    },
    {
        "id_room": "room003",
        "number": "125",
        "is_available": True
    },
    {
        "id_room": "room004",
        "number": "126",
        "is_available": True
    },
    {
        "id_room": "room005",
        "number": "127",
        "is_available": True
    }
]

hotels_data = [
    {
        "id_hotel": "3423423",
        "address": "körsbärsgatan 5A",
        "rooms": ["eqwewe", "sdadasdsa", "room003"]
    },
    {
        "id_hotel": "hotel002",
        "address": "Avenyn 10, Göteborg",
        "rooms": ["room004", "room005"]
    }
]

bookings_data = [
    {
        "hotel": "3423423",
        "room": "sdadasdsa",
        "customer": "34324234",
        "start_date": "2026-10-01",
        "end_date": "2026-10-05",
        "price": 320.00
    }
]

rooms = []
for room_data in rooms_data:
    room = Room(
        room_data["id_room"],
        room_data["number"],
        room_data["is_available"]
    )
    rooms.append(room)

hotels = []
for hotel_data in hotels_data:
    hotel = Hotel(
        hotel_data["id_hotel"],
        hotel_data["address"],
        [room for room in rooms if room.id_room in hotel_data["rooms"]]
    )
    hotels.append(hotel)

customers = []
for customer_data in customers_data:
    customer = Customer(
        customer_data["id_customer"],
        customer_data["name"],
        customer_data["age"]
    )
    customers.append(customer)

bookings = []
for booking_data in bookings_data:

    customer = next(
        customer for customer in customers
        if customer.id_customer == booking_data["customer"]
    )

    room = next(
        room for room in rooms
        if room.id_room == booking_data["room"]
    )

    hotel = next(
    hotel for hotel in hotels
    if hotel.id_hotel == booking_data["hotel"]
)
    booking = Booking(
        hotel,
        room,
        customer,
        booking_data["start_date"],
        booking_data["end_date"],
        booking_data["price"]
    )
    hotel.saveBooking(booking)
    bookings.append(booking)

def show_hotels():
    for hotel in hotels:
        print(hotel)

def show_available_rooms():
    for hotel in hotels:
        print("Hotel:", hotel.id_hotel)
        available_rooms = [room for room in hotel.checkAvailability()]
        print("Available rooms", *available_rooms)

def show_all_customers():
    print("Customers:", *[customer for customer in customers])

def register_customer():
   id_customer = str(uuid.uuid4())
   name = input("Type customer name: ")
   age = input("Type customer age: ")
   new_customer = Customer(id_customer, name, age)
   customers.append(new_customer)

def show_all_bookings():
    print("Bookings:", *[book for book in bookings])

def show_create_booking(hotels):
     print("=============================")
     print("       CHOOSE A HOTEL:        ")
     print("=============================")
     for hotel in hotels:
          print(hotel.id_hotel)

     selected_hotel_id = input("Hotel ID: ")
     selected_hotel = next(hotel for hotel in hotels if hotel.id_hotel == selected_hotel_id)
     show_available_rooms_menu(selected_hotel)

def show_available_rooms_menu(selected_hotel):
     print("=============================")
     print("      AVAILABLE ROOMS:       ")
     print("=============================")
     
     for available_room in selected_hotel.checkAvailability():
         print(available_room.number)

     room_number = input("Choose room number: ")
     selected_room = next((room for room in selected_hotel.checkAvailability() if room.number == room_number), None)
     show_customers(selected_hotel, selected_room) 
     

def show_customers(selected_hotel, selected_room):
    print("=============================")
    print("     CHOOSE CUSTOMER    ")
    print("=============================")

    for customer in customers:
        print(customer.name) # IN REAL WORLD CAN NOT BE NAME. IF HAVE TIME CHANGE IT.

    customer_name = input("Select a customer: ")
    selected_customer = next((customer for customer in customers if customer.name == customer_name), None)
    selected_dates(selected_hotel, selected_room, selected_customer)
    
def selected_dates(selected_hotel, selected_room, selected_customer):
     print("=============================")
     print("     SELECT START DATE:      ")
     print("=============================")

     start_date = input("Type start date: ")

     print("=============================")
     print("     SELECT END DATE:      ")
     print("=============================")

     end_date = input("Type end date: ")

     new_booking = Booking(selected_hotel, selected_room, selected_customer, start_date, end_date)
     # DO CONFIRM BOOKING SCREEN
     bookings.append(new_booking)

def cancel_booking():
     print("=============================")
     print("       CANCEL BOOKING        ")
     print("=============================")

     for book in bookings:
         print(book.id_booking)

     id_booking = input("Type booking ID: ")
     selected_booking = next((book for book in bookings if book.id_booking == id_booking), None)
     print(bookings)
     bookings.remove(selected_booking)


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
    option = int(input("Choose an option: "))

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
        show_create_booking(hotels)    
    elif option == 7:
        cancel_booking()
    elif option == 8:
        break   
    else:
        print("Please type an valid option")
        continue
