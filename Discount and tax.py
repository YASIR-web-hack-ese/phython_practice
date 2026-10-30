"""
A phone costs Rs 15,000. Apply a 10% discount, then add 18% tax to the discounted price,
 and print the final price. 
Now do it the other way round: tax first, then the discount. Do you get the same answer? 
Write a comment in your code explaining why or why not.
"""
phone_cost =15000
dicount_prize = 0.10
tax_prize =0.18
dicount_prize = phone_cost *(dicount_prize)#dicount prize 1500.
prize_after_dicount = phone_cost - (dicount_prize)
tax_prize = tax_prize *prize_after_dicount
final_prize=tax_prize+prize_after_dicount 
print(prize_after_dicount)
print(tax_prize)
print(final_prize)