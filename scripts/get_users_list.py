#!/usr/bin/env python3

import csv
import os
import requests


# Artifactory API URL
ARTIFACTORY_URL = os.getenv('ARTIFACTORY_TARGET_URL')

# Artifactory credentials
USERNAME = os.getenv('ARTIFACTORY_ADMIN_USER')
API_KEY = os.getenv('ARTIFACTORY_ADMIN_API_KEY')
    
# Function to fetch all users from Artifactory
def fetch_artifactory_users():
    try:
        response = requests.get(ARTIFACTORY_URL, auth=(USERNAME, API_KEY))
        response.raise_for_status()  # Raise an exception for HTTP errors
        users_data = response.json()
        return users_data
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)
        return None

# Function to write users data to CSV file
def write_users_to_csv(users_data):
    try:
        with open('artifactory_users.csv', mode='w', newline='') as file:
            fieldnames = ['Username', 'Email Address', 'Admin', 'Groups']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for user_data in users_data:
                writer.writerow({
                    'Username': user_data.get('name', ''),
                    'Email Address': user_data.get('email', ''),
                    'Admin': user_data.get('admin', False),
                    'Groups': ','.join(user_data.get('groups', []))
                })
        print("User data has been written to artifactory_users.csv successfully.")
    except Exception as e:
        print("Failed to write user data to CSV file:", e)

if __name__ == "__main__":
    users_data = fetch_artifactory_users()
    print(fetch_artifactory_users())
    if users_data:
        write_users_to_csv(users_data)
