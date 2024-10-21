# Encoder() made by Landen Parke
# parke.landen@ufl.edu


# Program Functions

def encode(password):
    encoded_password = ""
    for number in str(password):
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
        while True:
            try:
                password_input = input("Please enter your password: ")
                password_input = int(password_input) # If input has a letter than except will execute
            except:
                print("Please enter only numbers for your password.")
            if len(str(password_input)) != 8: # Makes sure that password is 8 characters long
                print("Password must be 8 characters long!")
            elif type(password_input) == int: # If the try: successfully executed than break while loop
                break
        password_storage = encode(password_input)
        print("Your password has been encoded and stored!\n")
    elif choice == 2:
        # TODO: add decoder()
        pass
    elif choice == 3:
        break
