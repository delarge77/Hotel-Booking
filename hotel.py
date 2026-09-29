class Hotel:
    def __init__(self, id_hotel, address, rooms) -> None:
        self.id_hotel = id_hotel
        self.address = address
        self.rooms = rooms
        self.bookings = []
    
    def checkAvailability(self):
        availableRooms = []
        for room in self.rooms:
            if room.is_available:
                availableRooms.append(room)       
        return availableRooms

    def cancelBooking(self, id_booking):
        book = next((book for book in self.bookings if book.id_booking == id_booking), None)
        if book is not None:
            if book.room.is_available == False:
                book.room.is_available = True
                self.bookings.remove(book)
        else:
            print("Booking dont exist")
    
    def saveBooking(self, book):
        if book.room.is_available == True:
            book.room.is_available = False
            self.bookings.append(book)
        else:
            print("Room is not available")
    
    def allBookings(self):
        return self.bookings
