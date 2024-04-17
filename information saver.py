import re

email_dict = {}
phone_dict = {}
password_dict = {}

def save_to_file(filename, dictionary):
    with open(filename, 'w') as f:
        for key, value in dictionary.items():
            f.write(f"{key},{value}\n")

def load_from_file(filename, dictionary):
    try:
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(',')
                dictionary[key] = bool(value)  # Convert string to boolean
    except FileNotFoundError:
        pass

def phoneNumbers():
    pattern = r"^\d{11}$"
    validate_phone_number = lambda phone_number: re.match(pattern, phone_number) is not None

    while True:
        Phone = input("Enter your phone number: ")
        
        if validate_phone_number(Phone):
            if Phone in phone_dict:
                print("Phone number '{}' already exists! Please enter a different one.".format(Phone))
            else:
                phone_dict[Phone] = True
                print("Phone number added successfully!")
                break
        else:
            print("Invalid phone number format. Please try again.")

def email():
    patternE =  r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    validate_email = lambda email: re.match(patternE, email) is not None

    while True:
        Email = input("Enter your email: ")
        
        if validate_email(Email):
            if Email in email_dict:
                print("Email '{}' already exists! Please enter a different one.".format(Email))
            else:
                email_dict[Email] = True
                print("Email added successfully!")
                break
        else:
            print("Invalid email format. Please try again.")

def password():
    while True:
        password = input('Enter your password: ')

        if len(password) < 8:
            print("Password must be at least 8 characters long. Please try again.")
        else:
            if password in password_dict:
                print("Password already exists! Please enter a different one.")
            else:
                password_dict[password] = True
                print("Password added successfully!")
                break

# Load existing data from files
load_from_file("emails.txt", email_dict)
load_from_file("phones.txt", phone_dict)
load_from_file("passwords.txt", password_dict)

# Call functions
email()
phoneNumbers()
password()

# Save data to files
save_to_file("emails.txt", email_dict)
save_to_file("phones.txt", phone_dict)
save_to_file("passwords.txt", password_dict)
