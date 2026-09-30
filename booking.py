from room import Room
from hotel import Hotel
import uuid 
class Booking:
    def __init__(self, hotel: Hotel, room: Room, customer, start_date, end_date, price) -> None:
        self.id_booking = str(uuid.uuid4())
        self.hotel = hotel
        self.room = room
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.price = price

    def __str__(self):
        return f"Id booking: {self.id_booking} hotel: {self.hotel} room:{self.room} customer: {self.customer}, start date:{self.start_date}, end date: {self.end_date}, price: {self.price}"


