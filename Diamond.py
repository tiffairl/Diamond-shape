"""To make diamond shape."""

def rows(letter):
    """Every diamond takes a letter, and outputs it for the shape."""
    distance = ord(letter) - ord('A')
    result = []

    for item in range(distance + 1):
        character = chr(ord('A') + item)

        if item == 0:
            row = ' ' * distance + 'A' + ' ' * distance
        else:
            outer = distance - item
            inner = 2 * item - 1
            row = (
                ' ' * outer +
                character +
                ' ' * inner +
                character +
                ' ' * outer
            )

        result.append(row)

    result.extend(result[-2::-1])

    return result