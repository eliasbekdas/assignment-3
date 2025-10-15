"""
DATA 4000 – Python with AI (Exceptions)
File: inventory_checker.py
Author: Elias Bekdas
Description: Check inventory vs reorder threshold with error handling.
"""

def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid entry. Please enter an integer.")

def main() -> None:
    while True:
        inventory = get_valid_int("Enter current inventory level: ")
        threshold = get_valid_int("Enter minimum reorder threshold: ")
        try:
            percent = (inventory / threshold) * 100
        except ZeroDivisionError:
            print("Threshold cannot be zero. Try again.\n")
            continue

        print(f"Inventory is {percent:.1f}% of threshold.")
        if inventory < threshold:
            print("Reorder alert: inventory below threshold!")
        else:
            print("Inventory level sufficient.")
        break

if __name__ == "__main__":
    main()