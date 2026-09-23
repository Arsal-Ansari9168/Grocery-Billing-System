#simple Grocery Billing System using a while loop and if-elif-else.

total = 0

while True:
    print("\n--- Grocery Billing System ---")
    print("1. Rice - ₹500")
    print("2. Wheat - ₹400")
    print("3. Sugar - ₹50")
    print("4. Milk - ₹60")
    print("5. Cooking Oil - ₹150")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        quantity = int(input("Enter quantity: "))
        total = total + (500 * quantity)
        print("Rice added to bill.")

    elif choice == 2:
        quantity = int(input("Enter quantity: "))
        total = total + (400 * quantity)
        print("Wheat added to bill.")

    elif choice == 3:
        quantity = int(input("Enter quantity: "))
        total = total + (50 * quantity)
        print("Sugar added to bill.")

    elif choice == 4:
        quantity = int(input("Enter quantity: "))
        total = total + (60 * quantity)
        print("Milk added to bill.")

    elif choice == 5:
        quantity = int(input("Enter quantity: "))
        total = total + (150 * quantity)
        print("Cooking Oil added to bill.")

    elif choice == 6:
        print("\n--- Final Bill ---")
        print("Subtotal: ₹", total)

        if total >= 2000:
            discount = total * 0.15
        elif total >= 1000:
            discount = total * 0.10
        elif total >= 500:
            discount = total * 0.05
        else:
            discount = 0

        final_bill = total - discount

        print("Discount: ₹", discount)
        print("Final Bill: ₹", final_bill)
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")