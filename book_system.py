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
    

for hotel in hotels:
    print("Hotel:", hotel.id_hotel)

    for booking in hotel.allBookings():
        print(booking)

# room1 = Room("eqwewe","123", False)
# room2 = Room("sdadasdsa","124")
# hotel = Hotel("3423423", "körsbärsgatan 5A", [room1, room2])

# customer1 = Customer("34324234","Alessandro",25)
# customer2 = Customer("34324235","Maria",21)

# Save the booking.
# Print hotel.allBookings().
# Print the room.
# Cancel the booking.
# Print hotel.allBookings() again.
# Print the room again.
# Try cancelling the same booking a second time.

# Then look at the results and tell me what you think should happen at step 7.
# booking1 = Booking(room2, customer1, "3764346", "6372462", 320.00)
# hotel.saveBooking(booking1)
# print(*hotel.allBookings())
# print(room2)
# print("FIRST",hotel.findBooking(booking1.id_booking))
# hotel.cancelBooking(booking1.id_booking)
# print(hotel.allBookings())
# print(room2)
# hotel.cancelBooking(booking1.id_booking)
# print(hotel.findBooking(booking1.id_booking))


# booking2 = Booking("4342342344", room2, customer2, "3764346", "6372462", 320.00)
# hotel.saveBooking(booking2)

# print(len(hotel.allBookings()))
# hotel.cancelBooking("4342342343")
# hotel.cancelBooking("4342342344")
# print(len(hotel.allBookings()))
# hotel.cancelBooking("naoexiste")










