
a = input("Enter status of Room A (Clean/Dirty): ").capitalize()
b = input("Enter status of Room B (Clean/Dirty): ").capitalize()
pos = input("Enter initial location (A/B): ").upper()

print("\nVacuum Cleaner Agent")
print("Goal: Clean both Room A and Room B\n")

while a == "Dirty" or b == "Dirty":
    print("Current location:", pos)
    print("Room A:", a, "| Room B:", b)

    if pos == "A":
        if a == "Dirty":
            print("Action: SUCK in Room A")
            a = "Clean"
        else:
            print("Action: MOVE RIGHT to Room B")
            pos = "B"
    else:
        if b == "Dirty":
            print("Action: SUCK in Room B")
            b = "Clean"
        else:
            print("Action: MOVE LEFT to Room A")
            pos = "A"

print("\nCurrent location:", pos)
print("Room A:", a, "| Room B:", b)
print("Goal Achieved! Both rooms are clean.")
