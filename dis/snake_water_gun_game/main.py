import random
computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (1 for snake, -1 for water, 0 for gun): ")
youdist = {"1": 1, "-1": -1, "0": 0}  
reversedist = {1: "snake", -1: "water", 0: "gun"}
you = youdist[youstr]

print(f"Computer chose: {reversedist[computer]}")

if (computer == you):
    print("You won! Snake beats snake.")

else:
    if(computer == -1 and you == 1):
        print("You lost! Water beats snake.")

    elif(computer == 1 and you == -1):
        print("You lost! Snake beats water.")

    elif(computer == -1 and you == -1):
        print("You won! Water beats water.")

    elif(computer == 0 and you == 1):
        print("You lost! Gun beats snake.")

    elif(computer == 0 and you == -1):
        print("You won! Water beats gun.")
    
    elif(computer == 0 and you == 0):
        print("You won! Gun beats gun.")

    elif(computer == 1 and you == 0):
        print("You won! Gun beats snake.")

    elif(computer == -1 and you == 0):
        print("You lost! Gun beats water.")

    elif(computer == 0 and you == 0):
        print("It's a tie! Gun vs Gun.")


    else:
        print("Invalid input! Please enter 1, -1, or 0.")
