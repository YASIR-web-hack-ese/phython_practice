"""Four friends split a Rs 4,750 dinner. Print each person's share using /. 
Then look up the // and % operators and use them to print 
how many whole rupees each person pays and how many rupees are left over.
"""
dinner_split =4750
frends_f = 4
bill_per_friend = dinner_split // frends_f
left_over = dinner_split %frends_f
share_per_person = dinner_split / frends_f
print("bill per person",bill_per_friend)
print("remender left person",left_over)
print("share per person",share_per_person)