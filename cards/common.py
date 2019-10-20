def get_deck():
    return [
        f'{number}{suit}'
        for number in list(range(2,11)) + ['J', 'Q', 'K', 'A']
        for suit in ['♠', '♥', '♦', '♣']
    ]