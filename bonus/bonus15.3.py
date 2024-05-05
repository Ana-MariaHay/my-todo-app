import json

with open("../files/qquestions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)

    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
message = ""
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "correct"
    else:
        result = "wrong"

    message = (f"Your answer for question {index + 1} was"
               f" {result} {question['user_choice']}."
               f" Correct answer {question['correct_answer']}.")

    print(message)

print(f"You scored {score} out of {len(data)}")
