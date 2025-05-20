# 🚀 Project: Random Name Ranking
# 🎯 Task:
# - Ask the user for four names.
# - Assign a random number (0-10) to each name.
# - Determine the ranking based on the highest number.
# - Declare Winner, Second Place, Third Place, and Runner-Up.

import random

name1=input("Enter First Name: ")
name1RandomNumber=random.randint(0, 10)

name2=input("Enter Second Name: ")
name2RandomNumber=random.randint(0, 10)

name3=input("Enter Third name: ")
name3randomNumber=random.randint(0, 10)

name4 = input("Enter Fourth Name: ")
name4RandomNumber = random.randint(0, 10)

names=[name1, name2, name3, name4]
values=[name1RandomNumber, name2RandomNumber, name3randomNumber, name4RandomNumber]

for i in range(len(values)):
    for j in range(i+1, len(values)):
        if values[i] < values[j]:
            values[i], values[j] = values[j], values[i]
            names[i], names[j] = names[j], names[i]

print("\nResults:")
print(f"{names[0]} is the Winner with a score of {values[0]}")
print(f"{names[1]} takes Second Place with a score of {values[1]}")
print(f"{names[2]} takes Third Place with a score of {values[2]}")
print(f"{names[3]} is the Runner-Up with a score of {values[3]}")

