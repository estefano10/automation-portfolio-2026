from member import Member
from session import Session
import pytest

@pytest.fixture
def session():
    return Session("Spinning", "2026-08-01", 2)

@pytest.fixture
def member():
    return Member("Kevin", "Premium")

@pytest.fixture
def unpaid_member():
    return Member("Morita", "Basic", False)


def test_new_session_starts_empty(session):
    assert session.available_spots() == 2

def test_book_takes_a_spot(session, member):
    booking = session.book(member)
    assert session.available_spots() == 1
    assert booking.is_confirmed
    assert len(session.bookings) == 1

def test_inactive_member_cannot_book(session):
    member = Member("Kevin", "Premium")
    member.cancel_membership()
    with pytest.raises(ValueError, match="Member is not active"):
        session.book(member)

def test_unpaid_member_cannot_book(session, unpaid_member):
    with pytest.raises(ValueError, match="Member is not paid up to date"):
        session.book(unpaid_member)

def test_full_session_cannot_book(session, member):
    session.book(Member("Nick", "Basic"))
    session.book(Member("Sofia", "Basic"))
    with pytest.raises(ValueError, match="Session is full"):
        session.book(member)

def test_cancelling_a_booking_frees_a_spot(session, member):
    booking1 = session.book(Member("Nick", "Basic"))
    booking2 = session.book(Member("Sofia", "Basic"))
    assert session.available_spots() == 0
    booking2.cancel()
    assert session.available_spots() == 1
    session.book(member)
    assert session.available_spots() == 0

@pytest.mark.parametrize("bookings_to_make, should_fit",[
    (1, True),
    (2, True),
    (3, True),
    (4, False)
] )
def test_capacity_limit(bookings_to_make, should_fit):
    session = Session("Spinning", "2026-08-01", 3)
    if should_fit:
        for i in range(bookings_to_make):
            session.book(Member(f"Socio{i}", "Basic"))
        assert session.available_spots() == 3 - bookings_to_make
    else:
        with pytest.raises(ValueError, match="Session is full"):
            for i in range(bookings_to_make):
                session.book(Member(f"Socio{i}", "Basic"))