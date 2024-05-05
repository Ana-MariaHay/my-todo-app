def password(length):
    if len(length) > 8:
        return True
    else:
        return False


print(password("ana maria hay"))
print("ana maria hay")
print(password("ana"))
print("ana")