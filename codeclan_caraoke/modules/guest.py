class Guest:

    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    def check_can_afford_admission(self, room):
        if self.cash >= 10:
            return True
        else:
            return False

    def pay_admission_fee(self, room):
        self.cash -= room.admission_fee

    def react_to_favourite_song(self, songs):
        if self.favourite_song in songs:
            return ("This is my jam")