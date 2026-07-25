from member import Member

def test_new_member_starts_active():
    e = Member("Estefano", "Premium", True, ["Kick boxing"])
    assert e.is_active

def test_cancel_membership_deactivates_member():
    m = Member("Morita", "Premium", False, ["Spinning"])
    m.cancel_membership()
    assert not m.is_active


def test_members_do_not_share_activities():
    member1 = Member("Nicolas", "Premium", True)
    member2 = Member("Kevin", "Premium", False)
    member1.enrolled_activities.append( "Weight training")
    assert member2.enrolled_activities == []
