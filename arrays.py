monthly_expenses = [2200, 2350, 2600, 2130, 2190, 0,0,0,0,0,0,0]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f"Difference between Feb and Jan: ${monthly_expenses[1] - monthly_expenses[0]}") # O(1)

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f"Expenses for the first quarter: ${sum(monthly_expenses[0:3])}") # O(1)

# 3. Find out if you spent exactly 2000 dollars in any month.
if 2000 in monthly_expenses: # O(n)
    index = monthly_expenses.index(2000)
    print(f"You spent 2000 on month {monthly_expenses[index]}.")
else:
    print("You did not spend exactly $2000 within any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
monthly_expenses[5] = 1980 # O(1)
print(f"June expenses: ${monthly_expenses[5]}")

# 5. You returned an item that you bought in a month of April and got a refund of 200$.
# Make a correction to your monthly expense list based on this.
print(f"April before refund: ${monthly_expenses[3]}")
monthly_expenses[3] -= 200 # O(1)
print(f"April after refund: ${monthly_expenses[3]}")




