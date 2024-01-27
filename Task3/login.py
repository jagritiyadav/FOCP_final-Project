import getpass
import hashlib
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def login(username, password, password_file="passwd.txt"):
    with open(password_file, "r") as file:
        for line in file:
            tmp = line.strip().split(":")
            stored_username, stored_password = tmp[0], tmp[-1].strip()
            if stored_username == username:
                print("Username found")
                entered_password = hash_password(password.strip())
                print("Access granted.")
                return
        print("Access denied.")

if __name__ == "__main__":
    username = input("User: ")
    password = getpass.getpass("Password: ")
    login(username, password)
