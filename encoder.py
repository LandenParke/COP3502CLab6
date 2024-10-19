# Encoder() made by Landen Parke
# parke.landen@ufl.edu


# Program Functions

def encode(password):
    encoded_password = ""
    for number in password:
        encoded_password += str(int(number)+3) # Convert to integer for adding 3 then convert back to string to create encoded password
    return encoded_password
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))
    return option

# Program loop

password_storage = "" # Variable for storing encoded passwords

while True:
    choice = menu()
    if choice == 1:
        password_storage = encode(input("Please enter your password: "))
        print("Your password has been encoded and stored!\n")
    elif choice == 2:
        # TODO: add decoder()
        pass
    elif choice == 3:
        break
