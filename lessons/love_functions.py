def love(name: str) -> str:
    """Given name as a parameter, returns a loving string."""
    return f"I love you {name}!!!!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        # Concatenation
        love_note = love_note + love(to) + "\n"
        counter = counter + 1
    return love_note