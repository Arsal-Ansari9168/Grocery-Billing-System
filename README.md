# 🛒 Grocery Billing System

## 📌 Project Overview

The Grocery Billing System is a simple Python-based console application used to calculate a customer's grocery bill.

The program provides a fixed list of grocery items with their prices. Customers can select multiple items, enter the quantity, and the program calculates the subtotal, discount, and final bill.

## 🛠️ Technologies Used

* Python
* while loop
* if-elif-else
* for loop
* User Input
* Arithmetic Operations

## 🛍️ Available Grocery Items

| No. | Item        | Price |
| --: | ----------- | ----: |
|   1 | Rice        |  ₹500 |
|   2 | Wheat       |  ₹400 |
|   3 | Sugar       |   ₹50 |
|   4 | Milk        |   ₹60 |
|   5 | Cooking Oil |  ₹150 |
|   6 | Exit        |     - |

## ⚙️ Features

* Display available grocery items.
* Select a grocery item.
* Enter the quantity.
* Calculate the price based on quantity.
* Purchase multiple items.
* Keep adding item prices to the total bill.
* Automatically calculate the discount.
* Display the subtotal.
* Display the discount amount.
* Display the final bill.
* Continue showing the menu until Exit is selected.

## 💰 Discount Rules

|       Subtotal |    Discount |
| -------------: | ----------: |
| ₹2000 or above |         15% |
| ₹1000 or above |         10% |
|  ₹500 or above |          5% |
|     Below ₹500 | No Discount |

## 🧮 Billing Calculation

The amount for an item is calculated using:

```python
amount = price * quantity
```

The total bill is calculated by adding the amount of each purchased item:

```python
total = total + amount
```

After the customer selects **Exit**, the program calculates the discount according to the subtotal.

## ▶️ How to Run

1. Install Python on your computer.
2. Open the project in VS Code or any Python IDE.
3. Open the Python file.
4. Run the program.
5. Select an item from the menu.
6. Enter the quantity.
7. Continue purchasing other items if required.
8. Select **6 - Exit** to generate the final bill.

## 💻 Example

```text
--- Grocery Billing System ---

1. Rice - ₹500
2. Wheat - ₹400
3. Sugar - ₹50
4. Milk - ₹60
5. Cooking Oil - ₹150
6. Exit

Enter your choice: 1
Enter quantity: 2

Rice added to bill.
Amount: ₹1000
```

After selecting Exit:

```text
--- Final Bill ---

Subtotal: ₹2000
Discount: ₹300
Final Bill: ₹1700

Thank you for shopping!
```

## 📚 Python Concepts Practiced

This project demonstrates the use of:

* Variables
* `while` loop
* `for` loop
* `if-elif-else`
* `input()`
* `int()`
* Arithmetic operators
* Conditional statements
* `break` statement

## 🎯 Project Objective

The main objective of this project is to understand how Python programming can be used to create a simple real-world **Grocery Billing System** using basic programming concepts.

## 👨‍💻 Author

**Arsal Ansari**

Python Beginner Project – Grocery Billing System    
