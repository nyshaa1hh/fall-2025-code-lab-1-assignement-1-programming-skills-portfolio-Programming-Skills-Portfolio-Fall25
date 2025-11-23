def biography():
    name = input("Enter your full name: ")
    hometown = input("Enter your home country: ")
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)
    else:
        age = "age is invalid!"
    return {"name": name, "hometown": hometown, "age": age}

def bio():
    user_information = biography()
    print(f"Name: {user_information['name']}\nHometown: {user_information['hometown']}\nAge: {user_information['age']}")                                                       
bio()
