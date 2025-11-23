password=12345
tries=0
attempts = 5

while tries < attempts:
    enter_password = input("Enter The password: ")
    if enter_password == password:
        print("correct password.approved")
        break
    else:
        tries += 1
        remaining = attempts - tries
        if remaining > 0:
            print(f"Wrong password. You have {remaining} attempts left.")
        else:
            print("Maximum attempts reached. You have been caught!")
