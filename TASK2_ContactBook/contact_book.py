FILE_NAME = "contacts.txt"

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def load_contacts():
    try:
        contacts = {}
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
        return contacts
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n----- CONTACT LIST -----\n")
        for name, phone in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {phone}")
            print("-" * 25)

def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()

    if name in contacts:
        print("\nContact Found")
        print(f"Name : {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()

        if not new_phone:
            print("Phone number cannot be empty.")
            return
        
        if not is_valid_phone(new_phone):
            print("Phone number must contain exactly 10 digits.")
            return
        contacts[name] = new_phone
        save_contacts(contacts)

        print("Contact updated successfully!")

    else:
        print("Contact not found.")

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

        if not is_valid_phone(phone):
            print("Phone number must contain exactly 10 digits.")
            continue

        if not name or not phone:
            print("Name and Phone Number cannot be empty!")
            continue

        contacts[name] = phone
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