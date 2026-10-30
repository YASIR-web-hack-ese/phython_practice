#varibales  A variable is a name that points to a value. You create one with =:

customer = "Noor Foods"
order_total = 12800
discount_rate = 0.1
is_paid = False
#every value has a type, which decides what you can do with it:

#Type	Example	Used for
#str (string)	"Noor Foods"	Text
#int (integer)	12800	Whole numbers
#float	0.1	Numbers with a decimal point
#bool (boolean)	True, False	Yes/no values

print(type(order_total))      # <class 'int'>

discount = order_total * discount_rate
final_total = order_total - discount
print(final_total) 

