choice: int = int(input("Enter a number."))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("D")
    else:
        print("C")