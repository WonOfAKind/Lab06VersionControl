# Original Code by Wonchae Lee

def encode(password):
    encoded_password = ''

    for i in password:
        number = int(i)
        encode_number = ''

        if number >= 7:
            encode_number = str((number + 3) % 10)
        else:
            encode_number = str(number + 3)

        encoded_password += encode_number

    return encoded_password


def main():
    loop = True

    while loop:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:
            password_encode = input("Please enter your password to encode: ")
            password_encoded = encode(password_encode)
            print("Your password has been encoded and stored!\n")
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            loop = False


if __name__ == "__main__":
    main()
