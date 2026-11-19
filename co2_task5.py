def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# Correct function
def add_item(item, order=None):

    if order is None:
        order = []

    order.append(item)
    return order


# Demonstrate the bug
print("Buggy Function:")

print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))


# Correct function
print("\nCorrect Function:")

customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# Positional, keyword and default parameters
def calculate_bill(item, price, quantity=1):

    total = price * quantity
    gst = total * 0.05

    return total, gst


print("\nBill Details:")

bill, gst_amount = calculate_bill("Tea", 15, quantity=2)

print("Bill:", bill)
print("GST:", gst_amount)


# Local and global scope
college = "Saveetha"

def show_college():

    subject = "Python"

    print("Local variable:", subject)
    print("Global variable:", college)


show_college()


# Global keyword
count = 0

def update_count():

    global count
    count += 1


update_count()

print("Global count:", count)


# Nonlocal scope
def outer_function():

    message = "Hello"

    def inner_function():

        nonlocal message
        message = "Welcome"

    inner_function()

    print("Nonlocal variable:", message)


outer_function()


# Display default values
print("\nDefault values:", add_item_buggy.__defaults__)
