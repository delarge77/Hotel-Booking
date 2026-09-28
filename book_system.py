from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer

room1 = Room("eqwewe","123")
room2 = Room("sdadasdsa","124")
hotel = Hotel("3423423", "körsbärsgatan 5A", [room1, room2])

customer1 = Customer("34324234","Alessandro",25)
customer2 = Customer("34324235","Maria",21)

booking1 = Booking("4342342343", room2, customer1, "3764346", "6372462", 320.00)
hotel.saveBooking(booking1)

booking2 = Booking("4342342344", room1, customer2, "3764346", "6372462", 320.00)
hotel.saveBooking(booking2)

print(len(hotel.allBookings()))
hotel.cancelBooking("4342342343")
hotel.cancelBooking("4342342344")
print(len(hotel.allBookings()))






