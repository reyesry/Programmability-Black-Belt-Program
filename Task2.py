
#Ryan Menard Reyes
#Task 1
#Blackbelt Apprentice Level 1

import random

x = random.randint(1,10)

while True:
    y = int(input("Guess the number: "));
    if y == x:
        print("Correct!");   
        break
    elif y!= x:
        print("Wrong, Try again!"); 
    

