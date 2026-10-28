# Expense Tracker - Installment 4: The Tracker Makes Decisions
# Author: Junsay, Geme Earl C.
# A simple expense tracker that calculates expenses, tax, and budget.

print("=" * 40)
print("        EXPENSE TRACKER")
print("    Know where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense                          (coming soon)")
print("  [2] View all expenses                       (coming soon)")
print("  [3] Show total spent                        (coming soon)")
print("  [4] Exit                                    (coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? $"))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? $"))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

subtotal = 0
subtotal += amount1
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print(f"Made by: {name} | Installment 4")
print("=" * 40)