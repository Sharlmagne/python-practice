heroes = ['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f"Length of the list of heroes: {len(heroes)}") #O(1)

# 2. Add 'black panther' at the end of this list
print(f"Question 2: {heroes}")
heroes.append("black panther") #O(1)
print(f"Question 2-b: {heroes}")

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.pop() #O(1)
heroes.insert(2, "black panther") #O(1)
print(f"Question 3: {heroes}")

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# heroes = ["doctor strange" if hero == "thor" else hero for hero in heroes if hero != "hulk"]
heroes[1:3]=['doctor strange']
print(f"Question 4: {heroes}")

# 5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes = sorted(heroes)
print(f"Question 5: {heroes}")