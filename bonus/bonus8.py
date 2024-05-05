j_date = input("enter journal date: ")

j_mood = input("how do you rate your mood for today from 1 - 10: ")

j_thoughts = input("let your thoughts flow:\n")

# msg = f"date: {j_date} mood: {j_mood} thoughts: {j_thoughts}"
# print(msg)

with open(f"../journal/{j_date}.txt", 'w') as file:
    file.write(j_mood + 2 * "\n")
    file.write(j_thoughts)

# If you want to get all the text as one single string, use read().
# If you want to get separate strings for each line, use readlines().