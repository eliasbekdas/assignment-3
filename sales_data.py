"""
DATA 4000 – Python with AI (Exceptions)
File: sales_data.py
Author: Elias Bekdas
Description: Safely get valid sales data and compute total revenue.
"""

def get_valid_number(prompt: str, number_type: type) -> float:
    """Prompt until a valid number of the given type is entered."""
    while True:
        try:
            return number_type(input(prompt).strip())
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main() -> None:
    units = get_valid_number("Enter number of units sold: ", int)
    price = get_valid_number("Enter price per unit: $", float)
    total = units * price
    print(f"\n✅ Total revenue = {units} × ${price:.2f} = ${total:.2f}")

if __name__ == "__main__":
    main()
