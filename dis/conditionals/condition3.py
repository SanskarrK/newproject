marks1 = int(input("Enter marks 1: "))

marks2 = int(input("Enter marks 2: "))

marks3 = int(input("Enter marks 3: "))

marks4 = int(input("Enter marks 4: "))

total_percentage = (100*(marks1 + marks2 + marks3 + marks4)) / 400

if(total_percentage >= 40 and marks1 >= 32 and marks2 >= 32 and marks3 >= 32 and marks4 >= 32):
    print("You are passed")

else:

    print("You are failed")
# This code calculates the total percentage of marks obtained in four subjects and checks if the student has passed or failed.