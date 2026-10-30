"""
1. Delivery Charge Problem

A customer, "Karachi Crafts", orders 3 lamps at Rs 2,400 each.
Delivery costs Rs 350.
Store each value in a variable, then print the order total
including delivery. Finally, print the type of the total.
"""

customer = "Karachi Crafts"
lamps = 3
price_per_lamp = 2400
delivery_cost = 350

order_total = (lamps * price_per_lamp) + delivery_cost

print("Customer:", customer)
print("Order Total:", order_total)
print("Type:", type(order_total))

