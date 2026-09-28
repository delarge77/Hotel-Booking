from room import Room
class Booking:
    def __init__(self, id_booking, room: Room, customer, start_date, end_date, price) -> None:
        self.id_booking = id_booking
        self.room = room
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.price = price


    def __str__(self):
        return f"{self.room}"


