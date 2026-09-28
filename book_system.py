from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer

room1 = Room("eqwewe","123")
room2 = Room("sdadasdsa","124", False)
hotel = Hotel("3423423", "körsbärsgatan 5A", [room1, room2])
customer = Customer("34324234","Alessandro",25)


print(room2)
booking = Booking("4342342343", room2, customer, "3764346", "6372462", 320.00)
hotel.saveBooking(booking)
print(len(hotel.allBookings()))
hotel.cancelBooking("4342342343")
print(len(hotel.allBookings()))
print(room2)





