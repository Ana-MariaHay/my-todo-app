import json

with open("../files/qquestions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)

    user_choice = int(input("Enter your answer: "))
    if user_choice == question["correct_answer"]:
        print("You are correct, well done!")
    else:
        print(f"Your answer is incorrect, the correct answer was {question["correct_answer"]}")

    go_ahead = input("Another question Y/N: ").capitalize()
    if go_ahead != "Y":
        break
