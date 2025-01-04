import json
import pickle
import os  # Module for file deletion
from datetime import datetime

def pki_to_json(cookie_file_path="./x_cookies.pkl", json_file_path="./x_cookies.json"):
    """
    Convert Pickle data to JSON and save it.
    """
    with open(cookie_file_path, 'rb') as cookie_file:
        data = pickle.load(cookie_file)

        # Convert Pickle data to JSON
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

    # Save the JSON data to a file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print("Successfully converted Pickle data to JSON file.")

def modify_cookie_expiry(json_file_path="./x_cookies.json", new_expiry_date="2025-12-31 23:59:59"):
    """
    Load JSON data and explicitly set the cookie expiration date.
    """
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Convert the input expiration date to a UNIX timestamp
    new_expiry_timestamp = int(datetime.strptime(new_expiry_date, "%Y-%m-%d %H:%M:%S").timestamp())

    # Update the cookie expiration date
    if isinstance(json_data, list):
        for cookie in json_data:
            if 'expiry' in cookie:
                cookie['expiry'] = new_expiry_timestamp
    elif isinstance(json_data, dict):
        if 'expiry' in json_data:
            json_data['expiry'] = new_expiry_timestamp

    # Save the updated data back to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    print(f"Successfully set the cookie expiration date to '{new_expiry_date}'.")

def json_to_pki(json_file_path="./x_cookies.json", cookie_file_path="./x_cookies.pkl"):
    """
    Convert JSON data back to Pickle and delete the existing Pickle file.
    """
    # Delete the existing Pickle file if it exists
    if os.path.exists(cookie_file_path):
        os.remove(cookie_file_path)
        print(f"Successfully deleted the existing Pickle file '{cookie_file_path}'.")

    # Save the JSON data as Pickle
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    with open(cookie_file_path, 'wb') as cookie_file:
        pickle.dump(json_data, cookie_file)

    print("Successfully converted JSON data back to Pickle file.")

# Execution example
if __name__ == "__main__":
    # Step 1: Convert Pickle data to JSON
    pki_to_json()

    # Step 2: Modify JSON data (explicitly set the expiration date)
    modify_cookie_expiry(new_expiry_date="2025-01-06 23:59:59")

    # Step 3: Delete the existing Pickle file and convert the updated JSON data back to Pickle
    json_to_pki()

