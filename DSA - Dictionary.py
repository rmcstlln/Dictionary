contact = {}

print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit")

while True:
    choice = input("\nWhat do you want to do?: ")

    if choice == '1':
        name = input("What is your full name?: ")
        age = int(input("What is your age?: "))
        address = input("What is your address: ")
        phone = int(input("What is your phone number?: "))
        contact[name] = {
            "Age": age,
            "Address": address,
            "Phone": phone
        }
        print(contact)
        print("Contact Saved!")

    elif choice == '2':
        search = input("Enter the full name you want to search: ")
        print(search + "'s Contact Details are:")
        print("Age:", contact[search]['Age'])
        print("Address:", contact[search]['Address'])
        print("Phone:", contact[search]['Phone'])

    elif choice == '3':
        exit()

