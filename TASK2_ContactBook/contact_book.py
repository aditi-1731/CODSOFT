FILE_NAME = "contacts.txt"

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def load_contacts():
    try:
        contacts = {}

        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split(",")

                contacts[name] = {
                    "phone": phone,
                    "email": email,
                    "address": address
                }

        return contacts
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, details in contacts.items():
            file.write(
                f"{name},{details['phone']},{details['email']},{details['address']}\n"
            )

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- CONTACT LIST -----\n")

    print(f"{'Name':<20} {'Phone':<15}")
    print("-" * 35)

    for name, details in contacts.items():
        print(f"{name:<20} {details['phone']:<15}")

def search_contact(contacts):

    print("\n1. Search by Name")
    print("2. Search by Phone Number")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ").strip()

        if name in contacts:

            details = contacts[name]

            print("\nContact Found")
            print(f"Name    : {name}")
            print(f"Phone   : {details['phone']}")
            print(f"Email   : {details['email']}")
            print(f"Address : {details['address']}")

        else:
            print("Contact not found.")

    elif choice == "2":

        phone = input("Enter phone number: ").strip()

        for name, details in contacts.items():

            if details["phone"] == phone:

                print("\nContact Found")
                print(f"Name    : {name}")
                print(f"Phone   : {details['phone']}")
                print(f"Email   : {details['email']}")
                print(f"Address : {details['address']}")
                return

        print("Contact not found.")

    else:
        print("Invalid choice.")

def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()
    address = input("Enter new address: ").strip()

    if not is_valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts(contacts)
    print("Contact updated successfully!")
    

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)

        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def show_statistics(contacts):
    print("\n----- CONTACT STATISTICS -----")
    print(f"Total Contacts : {len(contacts)}")

contacts = load_contacts()

while True:
    print("\n===== CONTACT BOOK =====\n")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contact Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        if not is_valid_phone(phone):
            print("Phone number must contain exactly 10 digits.")
            continue

        if not name or not phone:
            print("Name and Phone Number cannot be empty!")
            continue

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        save_contacts(contacts)
        print("Contact added successfully!")

    elif choice == "2":
        display_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        show_statistics(contacts)

    elif choice == "7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")