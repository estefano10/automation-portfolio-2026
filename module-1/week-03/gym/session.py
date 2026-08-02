from booking import Booking
class Session:
    def __init__(self, activity, date, max_capacity):
        self.activity = activity
        self.date = date
        self.max_capacity = max_capacity
        self.bookings = []

    def available_spots(self):
        return self.max_capacity - len([b for b in self.bookings if b.is_confirmed])


    def book(self, member):
        if not member.is_active:
            raise ValueError("Member is not active")
        if not member.is_paid_up:
            raise ValueError("Member is not paid up to date")
        if self.available_spots() == 0:
            raise ValueError("Session is full")
        new_booking = Booking(member, self)
        self.bookings.append(new_booking)
        return new_booking

    def __repr__(self):
        return f"Session(activity={self.activity!r}, date={self.date!r}, max_capacity={self.max_capacity})"