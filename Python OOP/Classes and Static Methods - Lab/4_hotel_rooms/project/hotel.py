from project.room import \
    Room


class Hotel:
    def __init__(self,name:str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls,stars_count:int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self,room:Room):
        self.rooms.append(room)

    def take_room(self, room_number:int,people):
        current_room = next(filter(lambda room: room.number == room_number,self.rooms))
        if current_room:
            current_room.take_room(people)

    def free_room(self,room_number:int):
        current_room = next(filter(lambda room: room.number == room_number,self.rooms))
        if current_room:
            current_room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        all_guests = sum(r.guests for r in self.rooms if r.is_taken)
        return f"Hotel {self.name} has {all_guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"





