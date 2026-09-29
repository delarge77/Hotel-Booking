from room import Room
from hotel import Hotel
from booking import Booking
from customer import Customer

room1 = Room("eqwewe","123", False)
room2 = Room("sdadasdsa","124")
hotel = Hotel("3423423", "körsbärsgatan 5A", [room1, room2])

customer1 = Customer("34324234","Alessandro",25)
customer2 = Customer("34324235","Maria",21)

# Save the booking.
# Print hotel.allBookings().
# Print the room.
# Cancel the booking.
# Print hotel.allBookings() again.
# Print the room again.
# Try cancelling the same booking a second time.

# Then look at the results and tell me what you think should happen at step 7.
booking1 = Booking(room2, customer1, "3764346", "6372462", 320.00)
hotel.saveBooking(booking1)
print(*hotel.allBookings())
print(room2)
print("FIRST",hotel.findBooking(booking1.id_booking))
hotel.cancelBooking(booking1.id_booking)
print(hotel.allBookings())
print(room2)
hotel.cancelBooking(booking1.id_booking)
print(hotel.findBooking(booking1.id_booking))


# booking2 = Booking("4342342344", room2, customer2, "3764346", "6372462", 320.00)
# hotel.saveBooking(booking2)

# print(len(hotel.allBookings()))
# hotel.cancelBooking("4342342343")
# hotel.cancelBooking("4342342344")
# print(len(hotel.allBookings()))
# hotel.cancelBooking("naoexiste")










