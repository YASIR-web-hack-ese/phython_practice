"""
Sales tax. An order's subtotal is Rs 7,200 and sales tax is 18%. 
Print the tax amount and the total with tax (expected: 1296.0 and 8496.0). 
Print the type of the tax amount. Why is it a float when the subtotal was an int?"""

sub_total =7200
sales_tax =18
tax_amount =sub_total*sales_tax /100;
total_amount= sub_total+tax_amount;
print(type(total_amount))
print(type(tax_amount))
print(total_amount)
print(tax_amount)