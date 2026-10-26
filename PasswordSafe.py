from cryptography.fernet import Fernet

# Create an encryption key the first time
try:
    with open("key.key", "rb") as f:
        key = f.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

fernet = Fernet(key)


# View saved passwords
def view():
    try:
        with open("passwords.txt", "rb") as f:
            for line in f:
                decrypted = fernet.decrypt(line.strip())
                print(decrypted.decode())
    except FileNotFoundError:
        print("No passwords saved yet.")


# Add a new password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    data = name + " | " + pwd

    encrypted = fernet.encrypt(data.encode())

    with open("passwords.txt", "ab") as f:
        f.write(encrypted + b"\n")

    print("Password saved and encrypted!")


# Main menu
while True:
    mode = input(
        "Would you like to add or view passwords "
        "(view/add/q)? "
    ).lower()

    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")