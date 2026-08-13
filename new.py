#this is a experiment file to check if the pull request goes through
#first pull and push
import hashlib
import os

DB_FILE = "users.txt"

def hash_password(password):
    """Encrypts a password using SHA-256 for security."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Asks for new credentials and appends them to the file."""
    username = input("Enter a new username: ").strip()
    password = input("Enter a new password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.\n")
        return

    # Check if user already exists
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                stored_user, _ = line.strip().split(",")
                if stored_user == username:
                    print("Username already exists!\n")
                    return

    hashed_pw = hash_password(password)
    
    # Save credential pair to text file
    with open(DB_FILE, "a") as f:
        f.write(f"{username},{hashed_pw}\n")
    print("Registration successful!\n")

def login_user():
    """Validates entered credentials against the data file."""
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not os.path.exists(DB_FILE):
        print("No users registered yet. Please register first.\n")
        return

    hashed_input_pw = hash_password(password)

    with open(DB_FILE, "r") as f:
        for line in f:
            # Split data by the comma delimiter
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username and stored_hash == hashed_input_pw:
                print("Login successful! Welcome onboard.\n")
                return True
                
    print("Invalid username or password.\n")
    return False

def main():
    """Main menu system wrapper."""
    while True:
        print("--- LOGIN SYSTEM ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
