import sys

sys.path.append("../../")
from cards.common import (
    get_face,
    get_faces,
    get_suit,
)


def is_fighting(card: str):
    """
    Determine if a given card is a 'fighting' card
    (i.e., does putting it down on the table trigger some kind of action)

    The fighting cards in Makao are 2s, 3s (cause the next player to take
    two or three cards respectively), 4s (cause the next player to lose turn),
    Js (demand a non-fighting card in your posession from all other players),
    Qs (can be played on anything unless a fighting card's action needs to be
    resolved, and anything can be played on top of them), K♠ (previous player
    has to take 5 cards unless they reciprocate with K♥), K♥ (next player
    has to take 5 cards unless they reciprocate with K♠), and As (change the
    current suit)
    """
    face = get_face(card)
    if face in (str(x) for x in range(5, 11)):
        return False

    if face == "K" and get_suit(card) in ("♦", "♣"):
        return False

    return True


def is_stairs(left: str, right: str):
    """
    Determine if a pair of cards (left and right) is a valid stair

    Stairs in Makao allow you to put down multiple cards in one turn,
    provided each pair of cards fulfills the following:

     - the card face is identical (e.g. '4♦', '4♣'), or
     - the suit is identical, and the faces differ by one
       (e.g. '4♦', '5♦')
    """
    left_face, right_face = (get_face(x) for x in (left, right))
    if left_face == right_face:
        return True

    left_suit, right_suit = (get_suit(x) for x in (left, right))
    if left_suit != right_suit:
        return False

    if all(x in ("2", "A") for x in (left_face, right_face)):
        return True

    faces = get_faces()
    face_count = len(faces)

    left_idx, right_idx = (faces.index(x) for x in (left_face, right_face))

    return abs(left_idx - right_idx) == 1
