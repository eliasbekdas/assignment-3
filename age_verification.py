"""
DATA 4000 – Python with AI (Exceptions)
File: age_verification.py
Author: Elias Bekdas
Description: Verify customer age for marketing eligibility.
"""

def get_customer_age() -> int:
    while True:
        try:
            age = int(input("Enter customer's age: ").strip())
            if age <= 0:
                print("Age must be positive.")
                continue
            return age
        except ValueError:
            print("❌ Please enter a whole number for age.")
        except NameError:
            # Example only (commented variable would trigger this)
            print("⚠️  A variable was referenced before assignment.")

def main() -> None:
    age = get_customer_age()
    if age >= 18:
        print("✅ Customer is eligible for age-restricted promotions.")
    else:
        print("🚫 Customer is NOT eligible (must be 18+).")

if __name__ == "__main__":
    main()
