import random

def game():
    print("you are playing game.")
    score = random.randint(1, 100)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is: {score}")
    if score > hiscore:
        print("Congratulations! You have a new high score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"Your high score is: {hiscore}")

game