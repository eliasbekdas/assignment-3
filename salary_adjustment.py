"""
DATA 4000 – Python with AI (Exceptions)
File: salary_adjustment.py
Author: Elias Bekdas
Description: Simulate employee salary adjustment with error handling.
"""

def get_valid_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("❌ Please enter a valid number.")

def main() -> None:
    salary = get_valid_float("Enter current salary: $")
    while True:
        try:
            percent = get_valid_float("Enter adjustment percentage (0-100): ")
            if percent < 0:
                raise ValueError("Percentage cannot be negative.")
            if percent > 100:
                print("⚠️  Percentage unusually high — recheck value.")
            new_salary = salary * (1 + percent / 100)
            print(f"\n✅ New salary after {percent:.2f}% adjustment: ${new_salary:,.2f}")
            break
        except ValueError as e:
            print(f"Error: {e}. Try again.")

if __name__ == "__main__":
    main()
