def printPokerCard(cards):
    """Print multiple cards side by side."""
    # Initialize lists for card rows
    rows = [""] * 5
    # Format each card and add its lines to the respective row
    for card in cards:
        card_lines = format_card(card["card"], card["pattern"])
        for i in range(5):
            rows[i] += card_lines[i] + "  "  # Add spacing between cards

    # Print all rows
    for row in rows:
        print(row)

def format_card(value, suit):
    """Format a single card as a string."""
    return [
        "+------+", 
        f"| {value:<2}   |", 
        f"|  {suit}   |", 
         f"|  {value:>2}  |", 
        "+------+"
    ]