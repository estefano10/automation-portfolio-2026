class Member:
    def __init__(self, name, plan, is_paid_up=True, activities=None):
        self.name = name
        self.plan = plan
        self.is_paid_up = is_paid_up
        self.activities = activities or []
        self.is_active = True

    def cancel_membership(self):
        self.is_active = False

    def __repr__(self):
        return f"Member(name={self.name!r}, plan={self.plan!r}, active={self.is_active})"
    