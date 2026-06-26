import random
import string

print("\n" + "=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

def get_choice(message):
    while True:
        choice = input(message).strip().lower()

        if choice in ("y", "n"):
            return choice == "y"

        print("Please enter only 'y' or 'n'.")

def generate_password(length, upper, lower, digits, special):
    characters = ""
    password = []

    if upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if digits:
        characters += string.digits
        password.append(random.choice(string.digits))

    if special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        return None

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


while True:

    # Password Length
    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password must be at least 4 characters long.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Complexity Options
    upper = get_choice("Include Uppercase Letters? (y/n): ")
    lower = get_choice("Include Lowercase Letters? (y/n): ")
    digits = get_choice("Include Numbers? (y/n): ")
    special = get_choice("Include Special Characters? (y/n): ")

    # Generate Password
    password = generate_password(length, upper, lower, digits, special)

    if password:
        print("\nGenerated Password:", password)
    else:
        print("\nPlease select at least one character type.")
        continue

    # Generate Another password
    while True:
        again = input("\nGenerate another password? (y/n): ").strip().lower()

        if again == "y":
            break

        elif again == "n":
            print("\nThank you for using Password Generator!")
            exit()

        else:
            print("Please enter only 'y' or 'n'.")