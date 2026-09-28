class Booking:
    def __init__(self, room, customer, start_date, end_date, price) -> None:
        self.room = room
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.price = price