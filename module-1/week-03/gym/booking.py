class Booking:
    def __init__(self, member, session):
        self.member = member
        self.session = session
        self.is_confirmed = True

    def cancel(self):
        self.is_confirmed = False

    def __repr__(self):
        return f"Booking(member={self.member!r}, session={self.session}, is_confirmed={self.is_confirmed})"