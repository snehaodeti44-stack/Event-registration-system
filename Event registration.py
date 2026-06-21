event registration.py
# Event Registration System

participants = []

def register_event():
    name = input("Enter Participant Name: ")
    email = input("Enter Email: ")
    event = input("Enter Event Name: ")

    participants.append({
        "Name": name,
        "Email": email,
        "Event": event
    })

    print("\nRegistration Successful!\n")

def display_participants():
    print("\nRegistered Participants:")
    for p in participants:
        print(f"Name: {p['Name']}, Email: {p['Email']}, Event: {p['Event']}")

while True:
    print("\n--- Event Registration System ---")
    print("1. Register Participant")
    print("2. View Participants")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_event()
    elif choice == "2":
        display_participants()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice. Try Again.")
