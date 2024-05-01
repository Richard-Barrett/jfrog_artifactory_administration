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
        print("Users data retrieved successfully:", users_data)  # Debugging print
        return users_data
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)
        return None


# Function to fetch user details by username
def fetch_user_details(username):
    try:
        user_details_url = f"{ARTIFACTORY_URL}/{username}"
        response = requests.get(user_details_url, auth=(USERNAME, API_KEY))
        response.raise_for_status()  # Raise an exception for HTTP errors
        user_details = response.json()
        return user_details
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching details for user {username}:", e)
        return None

# Function to write user details to CSV file
def write_user_details_to_csv(user_details_list):
    try:
        print("Writing user details to CSV file...")  # Debugging print
        with open('artifactory_user_details.csv', mode='w', newline='') as file:
            fieldnames = ['Username', 'Email', 'Admin', 'PolicyViewer', 'PolicyManager', 'WatchManager', 'ReportsManager', 'ProfileUpdatable', 'InternalPasswordDisabled', 'Groups', 'LastLoggedIn', 'Realm', 'OfflineMode', 'DisableUIAccess', 'MFAStatus', 'Status', 'ShouldInvite']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for user_details in user_details_list:
                writer.writerow({
                    'Username': user_details['name'],
                    'Email': user_details.get('email', ''),
                    'Admin': user_details.get('admin', False),
                    'PolicyViewer': user_details.get('policyViewer', False),
                    'PolicyManager': user_details.get('policyManager', False),
                    'WatchManager': user_details.get('watchManager', False),
                    'ReportsManager': user_details.get('reportsManager', False),
                    'ProfileUpdatable': user_details.get('profileUpdatable', False),
                    'InternalPasswordDisabled': user_details.get('internalPasswordDisabled', False),
                    'Groups': ','.join(user_details.get('groups', [])),
                    'LastLoggedIn': user_details.get('lastLoggedIn', ''),
                    'Realm': user_details.get('realm', ''),
                    'OfflineMode': user_details.get('offlineMode', False),
                    'DisableUIAccess': user_details.get('disableUIAccess', False),
                    'MFAStatus': user_details.get('mfaStatus', ''),
                    'Status': user_details.get('status', ''),
                    'ShouldInvite': user_details.get('shouldInvite', False)
                })
        print("User details have been written to artifactory_user_details.csv successfully.")
    except Exception as e:
        print("Failed to write user details to CSV file:", e)


if __name__ == "__main__":
    users_data = fetch_artifactory_users()
    if users_data:
        print("Response from Artifactory API:", users_data)  # Debugging print
        if isinstance(users_data, list):  # Check if the response is a list of user dictionaries
            user_details_list = []
            for user in users_data:
                user_details = fetch_user_details(user["name"])
                if user_details:
                    user_details_list.append(user_details)
                    print("User details for", user["name"], ":", user_details)
            if user_details_list:
                write_user_details_to_csv(user_details_list)
            else:
                print("No user details found.")
        else:
            print("Unexpected response format. Expected a list of user dictionaries.")
    else:
        print("No response data from Artifactory API.")

