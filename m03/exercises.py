"""
Solutions to exercises 7.4, 7.5, 7.6, 7.7, 9.1, and 9.2
"""

# Exercise 7.4
# Make a list called things with these three strings as elements:
# "mozzarella", "cinderella", "salmonella"
things = ["mozzarella", "cinderella", "salmonella"]
print("7.4 - Initial list:")
print(things)
print()

# Exercise 7.5
# Capitalize the element in things that refers to a person and then print the list.
# Did it change the element in the list?
things[1] = things[1].capitalize()
print("7.5 - After capitalizing 'cinderella':")
print(things)
print("Yes, it changed the element in the list.")
print()

# Exercise 7.6
# Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print("7.6 - After making 'mozzarella' uppercase:")
print(things)
print()

# Exercise 7.7
# Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[2]
print("7.7 - After deleting 'salmonella':")
print("You deleted the salmonella! Here's your Nobel Prize.")
print(r"""
      .---.
    .'     '.
   /  .---.  \
  /  / _   \  \
 /  / (o)   \  \
|  |      |  |  |
|  |   A  |  |  |
 \  \     /  /
  \  '---'  /
   '.     .'
     '---'
   NOBEL PRIZE
""")
print(things)
print()

# Exercise 9.1
# Define a function called good() that returns the following list:
# ['Harry', 'Ron', 'Hermione']
def good():
    return ['Harry', 'Ron', 'Hermione']

print("9.1 - Calling good() function:")
print(good())
print()

# Exercise 9.2
# Define a generator function called get_odds() that returns the odd numbers
# from range(10). Use a for loop to find and print the third value returned.
def get_odds():
    for number in range(10):
        if number % 2 == 1:
            yield number

print("9.2 - Finding the third odd number:")
count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print(f"The third odd number is: {odd}")
        break
