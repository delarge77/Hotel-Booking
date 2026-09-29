from room import Room
class Booking:
    def __init__(self, id_booking, room: Room, customer, start_date, end_date, price) -> None:
        self.id_booking = id_booking # Generate a random number thought function
        self.room = room
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.price = price

    def __str__(self):
        return f"Id booking: {self.id_booking} room:{self.room} customer: {self.customer}, start date:{self.start_date}, end date: {self.end_date}, price: {self.price}"


