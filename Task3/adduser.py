import getpass
import hashlib
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def add_user(username, real_name, password, password_file="passwd.txt"):
    hashed_password = hash_password(password)
    
    with open(password_file, "a") as file:
        file.write(f"{username}:{real_name}:{hashed_password}\n")
    
    print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")
    password = hash_password(password)
    # Check if the username already exists
with open(r"C:\Users\DELL\Desktop\Task3\passwd.txt", "r+") as file:
    existing_usernames = [line.split(":")[0] for line in file.readlines()]

    if username in existing_usernames:
        print("Cannot add. Most likely username already exists.")
    else:
        add_user(username, real_name, password)