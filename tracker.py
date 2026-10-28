# Expense Tracker - Installment 2: Talking to the User
# Author: Junsay, Geme Earl C.
# A simple expense tracker that asks the user for two expenses.

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

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? $"))

total = amount1 + amount2
average = total / 2

print("\n" + "-" * 40)
print("SUMMARY")
print(f"  - {item1}:     ${amount1}")
print(f"  - {item2}:      ${amount2}")
print(f"Total spent:    ${total}")
print(f"Average:        ${average}")
print("-" * 40)
print(f"Made by: {name} | Installment 2")
print("=" * 40)