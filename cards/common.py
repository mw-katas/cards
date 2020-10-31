def get_faces():
    """
    Returns all standard playing card faces, starting at 2:

    >>> get_faces()
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    """
    return [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']

def get_deck():
    """
    Returns a standard deck of 52 playing cards:

    >>> get_deck()
    ['2♠', '2♥', '2♦', '2♣', '3♠', '3♥', '3♦', '3♣', '4♠', '4♥', '4♦', '4♣', '5♠', '5♥', '5♦', '5♣', '6♠', '6♥', '6♦', '6♣', '7♠', '7♥', '7♦', '7♣', '8♠', '8♥', '8♦', '8♣', '9♠', '9♥', '9♦', '9♣', '10♠', '10♥', '10♦', '10♣', 'J♠', 'J♥', 'J♦', 'J♣', 'Q♠', 'Q♥', 'Q♦', 'Q♣', 'K♠', 'K♥', 'K♦', 'K♣', 'A♠', 'A♥', 'A♦', 'A♣']

    >>> len(get_deck())
    52
    """
    return [
        f'{number}{suit}'
        for number in get_faces()
        for suit in ('♠', '♥', '♦', '♣')
    ]

def get_suit(card: str):
    """
    Returns a suit of a given card:

    >>> get_suit('A♣')
    '♣'

    >>> get_suit('10♣')
    '♣'
    """
    return card[-1]

def get_face(card: str):
    """
    Returns the face of a given card:

    >>> get_face('A♣')
    'A'

    >>> get_face('10♥')
    '10'
    """
    return card[:-1]