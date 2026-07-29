import pytest
from member import Member

@pytest.fixture
def member():
    return Member("Estefano", "Premium")

@pytest.fixture
def second_member():
    return Member("Morita", "Basic")

def test_new_member_starts_active(member):
    assert member.is_active
    assert member.name == "Estefano"
    assert member.plan == "Premium"

def test_cancel_membership_deactivates_member(member):
    member.cancel_membership()
    assert not member.is_active


def test_members_do_not_share_activities(member, second_member):
    member.enrolled_activities.append("Weight training")
    assert member.enrolled_activities == ["Weight training"]
    assert second_member.enrolled_activities == []