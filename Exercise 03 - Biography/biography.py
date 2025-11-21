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
    bio = biography()
    print("Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")
bio()
