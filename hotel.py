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
        book = self.findBooking(id_booking)
        if book is not None:
            if book.room.is_available == False:
                book.room.is_available = True
                self.bookings.remove(book)
        else:
            print("Booking dont exist")

    def findBooking(self, id_booking):
        return next((book for book in self.bookings if book.id_booking == id_booking), None)
    
    def saveBooking(self, book):
        if book.room.is_available == True and book.room in self.rooms:
            book.room.is_available = False
            self.bookings.append(book)
        else:
            print("Room is not available")
    
    def allBookings(self):
        return self.bookings

    def __str__(self) -> str:
        return f"{self.id_hotel}, {self.address}, {self.rooms}, {self.bookings}"