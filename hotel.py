class Hotel:
    def __init__(self, id_hotel: int, address: str, rooms) -> None:
        self.id_hotel = id_hotel
        self.address = address
        self.rooms = rooms

    availableRooms = []
    def checkAvailability(self):
        for room in self.rooms:
            if room.is_available:
                self.availableRooms.append(room)       
        return self.availableRooms

    def cancelBooking(self, id_booking):
        book = next((book for book in self.bookings if book.id_booking == id_booking), None)
        if book is not None:
            if book.room.is_available == False:
                print("PASSOU AQUI 4")
                book.room.is_available = True
                self.bookings.remove(book)
    
    bookings = []
    def saveBooking(self, book):
        if book.room.is_available == True:
            book.room.is_available = False
            self.bookings.append(book)
        ValueError("Room is not available")
    
    def allBookings(self):
        return self.bookings
