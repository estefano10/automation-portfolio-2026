class Session:
    def __init__(self, activity, date, max_capacity):
        self.activity = activity
        self.date = date
        self.max_capacity = max_capacity

    def __repr__(self):
        return f"Session(activity={self.activity!r}, date={self.date!r}, max_capacity={self.max_capacity})"