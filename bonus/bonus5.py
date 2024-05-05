mailing_list = ["sen", "ben", "john"]
# reverse = false is default (ascending order), reverse = true, sets the list to sort in descending order
mailing_list.sort(reverse=True)
print(mailing_list)
for index, item in enumerate(mailing_list):
    row = f"{index+1}) {item.capitalize()}"
    print(row)