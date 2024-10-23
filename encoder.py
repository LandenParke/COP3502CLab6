# Encoder() made by Landen Parke
# parke.landen@ufl.edu
# Decoder() made by Dajana Seitllari


# Program Functions

def encode(password):
    encoded_password = ""
    for number in str(password):
        encoded_password += str(int(number)+3) # Convert to integer for adding 3 then convert back to string to create encoded password
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for number in str(encoded_password): #get the stored encoded password and look at each number in the password
        decoded_password += str(int(number)-3) # Subtract 3 from the number
    return decoded_password

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
        if password_storage:
            decoded_password = decode(password_storage)
            print(f"The encoded password is: {password_storage} , and the original password is {decoded_password}.")
            print("")
        else:
            print("There was no password encoded to decode.") #else if there was nothing to decode
    elif choice == 3:
        break
