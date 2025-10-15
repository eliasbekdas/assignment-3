"""
DATA 4000 – Python with AI (Exceptions)
File: financial_ratio.py
Author: Elias Bekdas
Description: Calculate profit-margin ratio with defensive programming.
"""

def main() -> None:
    while True:
        try:
            profit = float(input("Enter profit: $").strip())
            revenue = float(input("Enter revenue: $").strip())
            ratio = (profit / revenue) * 100
        except ValueError:
            print("❌ Invalid number. Try again.\n")
            pass
        except ZeroDivisionError:
            print("⚠️  Revenue cannot be zero. Try again.\n")
            pass
        else:
            print(f"\n✅ Profit margin: {ratio:.2f}%")
            break

if __name__ == "__main__":
    main()
