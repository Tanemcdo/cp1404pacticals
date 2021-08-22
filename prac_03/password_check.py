
PASSWORD_LENGTH = 6


def main():
    password = get_password()
    display_password_length(password)


def get_password():
    password = input("Please enter password\n>> ")
    while len(password) < PASSWORD_LENGTH:
        password = input("Password must be {} letters or over\n>> ".format(PASSWORD_LENGTH))
    return password


def display_password_length(valid_password):
    for i in valid_password:
        print("*", end="")


main()
