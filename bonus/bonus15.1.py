import json
import random

with open("../files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
noq = len(data)
lower_bound = 0
upper_bound = noq - 1

while True:
    # Pick a random int using randint()
    rand = random.randint(lower_bound, upper_bound)
    #  print(rand, lower_bound, upper_bound)
    question = data[rand]

    print("\n" * 6)  # clear screen
    print(question["question"])
    print("A", question["A"])
    print("B", question["B"])
    print("C", question["C"])
    print("D", question["D"])
    ans = input("Select the correct option A, B, C, D or eXit: ")
    ans = ans.capitalize()

    if ans in "ABCDX":
        if ans == question["answer"]:
            print("You are correct, well done!")
        else:
            print(f"Your answer is incorrect, the correct answer was {question["answer"]}")
    else:
        print("You entered an invalid selection!")

    go_ahead = input("Another question Y/N: ").capitalize()
    if go_ahead != "Y":
        break
