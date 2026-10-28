# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Junsay, Geme Earl C.
# A simple expense tracker that tracks expenses and budget.

print("=" * 40)
print("        EXPENSE TRACKER")
print("    Know where your money goes.")
print("=" * 40)

name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0

while True:
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        print(f"Expenses:     {count}")
        print(f"Subtotal:     ${subtotal}")
        print(f"Tax ({tax_percent}%): ${tax}")
        print(f"Grand total:  ${total}")

        if total > budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: {name} | Installment 5")
        print("=" * 40)
        break

    else:
        print("Please choose 1, 2, 3 or 4.")