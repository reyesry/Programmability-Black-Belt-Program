"""
Ryan Menard Reyes
Task 2
"""
import random
x = random.randint(1,10)

while True:
    y = int(input("Guess the number: "));
    if y == x:
        print("Correct!");   
        break
    elif y!= x:
        print("Wrong, Try again!"); 
    

