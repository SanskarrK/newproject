import random

n = random.randint(1, 100)
a = -1
gusses = 0
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while(a != n):
    gusses += 1
    a = int(input("Enter your guess: "))
    if a < n:
        print(f"Congratulations! You've guessed the number {n} in {gusses} tries. Your guess was too low.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {gusses} tries. Your guess was too high.")

print(f"Congratulations! You've guessed the number {n} in {gusses} tries. Your guess was correct.")