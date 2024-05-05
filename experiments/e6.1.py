# file read, add a member and file write for .TXT
#
new_member = input("Enter a new member: ")
file = open('../files/members.txt', 'r')
members = file.readlines()
print(members)
file.close()

members.append(new_member + "\n")
print(members)
file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()