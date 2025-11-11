
   # Guessing Number Project

import random
while True:    

    num = random.randint(1,10)
    count = 0

    while True:
        guess = int(input("Enter the Number from 1 to 10 :  "))

        
        if guess>num:
            count+=1
            print("Go little Low")
        elif guess<num:
            count+=1
            print("Go little High")
        else:
            count+=1
            print(f"You guess the Right Number in {count} attempt")
            break
    another = input("Do you want play more ?  (y/n)")

    if another.lower() != "y":
          print(f"\nGame Closed\n")
          break
   
    