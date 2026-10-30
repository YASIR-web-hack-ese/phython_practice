""" A shop is shipping 23 items, and each box holds 6. 
Using only arithmetic (no if), print the number of full boxes, 
the number of items left over, and the total number of boxes needed, 
including a partly full one (expected: 3, 5 and 4). 
Each box costs Rs 120 to ship: print the shipping cost. 
Test your code with 24 items. Does the box count still come out right?"""

total_iteams = 23
each_box_holds =6
shepping_cost_per_box = 120
left_over_iteams = total_iteams % each_box_holds
full_boxes = total_iteams //6
taotal_boxes = (each_box_holds+ total_iteams -1 )//each_box_holds
shepping_cost_per_box = taotal_boxes + shepping_cost_per_bo
print(full_boxes)
print(left_over_iteams)
print(taotal_boxes)
print(shepping_cost_per_box)

total_iteams = 24
each_box_holds =6
shepping_cost_per_box = 120
left_over_iteams = total_iteams % each_box_holds
full_boxes = total_iteams //6
taotal_boxes = (each_box_holds+ total_iteams -1 )//each_box_holds
shepping_cost_per_box = taotal_boxes + shepping_cost_per_box
print(full_boxes)
print(left_over_iteams)
print(taotal_boxes)
print(shepping_cost_per_box)