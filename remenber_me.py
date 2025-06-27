from pathlib import Path
import json
def get_user_info(username: str, password: str, email: str):
    if not username or not password or not email:
        raise ValueError("Username, password, and email cannot be empty.")
    user_info = {
        "username": username,
        "password": password,
        "email": email
    }
    return user_info

def save_user_info(user_info: dict):
    with open(path, 'w') as file:
        json.dump(user_info, file, indent=4)
    print(f"User info saved to {path}")
def load_user_info():
    if not path.exists():
        print(f"No user info found at {path}.")
        return None
    with open(path, 'r') as file:
        user_info = json.load(file)
    return user_info

username = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")
user_info = get_user_info(username, password, email)
path = Path("user_info.json")
save_user_info(user_info)
loaded_info = load_user_info()
if loaded_info:
    print("Loaded user info:")
    for key, value in loaded_info.items():
        print(f"  {key}: {value}")  
# This code allows you to input user information, save it to a JSON file, and load it back.
# It ensures that the username, password, and email are not empty before saving.
