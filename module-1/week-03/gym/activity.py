class Activity:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor

    def __repr__(self):
        return f"Activity(name={self.name!r}, instructor={self.instructor!r})"