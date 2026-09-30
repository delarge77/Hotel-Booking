from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer

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

def show_create_booking(hotels):
     print("Choose hotel:")
     for hotel in hotels:
          print(hotel.id_hotel)

     selected_hotel_id = input("Hotel ID: ")
     selected_hotel = next(hotel for hotel in hotels if hotel.id_hotel == selected_hotel_id)
     show_available_rooms_menu(selected_hotel.checkAvailability())

def show_available_rooms_menu(available_rooms):
     print("Avaibale rooms:")
     for available_room in available_rooms:
          print(available_room.number)
     room = input("Choose room number: ")
    #  TODO continue from here !!! 

option = 0
while option != 7:
    print("=============================")
    print("   HOTEL BOOKING SYSTEM")
    print("=============================")
    print("1. Show hotels")
    print("2. Show available rooms")
    print("3. Show customers")
    print("4. Show bookings")
    print("5. Make a booking")
    print("6. Cancel a booking")
    print("7. Exit")
    option = int(input("Choose an option:"))

    if option == 1:
        for hotel in hotels:
            print(hotel)
    elif option == 2:
        for hotel in hotels:
            print("Hotel:", hotel.id_hotel)
            available_rooms = [room for room in hotel.checkAvailability()]
            print("Available rooms", *available_rooms)
    elif option == 3:
        print("Customers:", *[customer for customer in customers])
    elif option == 4:
        print("Bookings:", *[book for book in bookings])
    elif option == 5:
            show_create_booking(hotels)    
    elif option == 6:
            print("Cancel a booking")
    elif option == 7:
        break   
    else:
        print("Please type an valid option")
        continue












