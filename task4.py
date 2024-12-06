# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

Number=int(input("Please enter a number less than 10:"))

if 0 <Number< 10:
    print(f"{people[Number]}")

else:
    print("DO A NUMBER LESS THAN 10")