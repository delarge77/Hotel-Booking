class Room:
    def __init__(self,id_room, number, is_available = True):
        self.id_room = id_room
        self.number = number
        self.is_available = is_available

    def changeAvailibility(self):
        self.is_available = not(self.is_available)

    def __str__(self):
        return f"{self.id_room} {self.number}, {self.is_available}"