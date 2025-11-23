def biography():
    name = input("Enter your full name: ")
    hometown = input("Enter your home country: ")
    age = input("Enter your age: ")
    sex= input("Enter your gender: ")
    if age.isdigit():
        age = int(age)
    else:
        age = "age is invalid!"
    return {"name": name, "country": hometown, "age": age, "gender": sex}

def bio():
    bio = biography()
    print(f"Name: {bio['name']}\nCountry: {bio['country']}\nAge: {bio['age']}\nGender: {bio['gender']}")                                                       
bio()
