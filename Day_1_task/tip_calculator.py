# This program calculates tip amount and total bill.

# return sends value back from function.
# print only displays output on screen.

def calculate_tip(bill, tip_percent):
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount

    return {
        "tip": tip_amount,
        "total": total
    }

bills = [1000, 2500, 5000]

for bill in bills:
    result = calculate_tip(bill, 10)

    print(f"\nBill Amount: ₹{bill}")
    print(f"Tip Amount: ₹{result['tip']}")
    print(f"Total Amount: ₹{result['total']}")