import time

import requests


class FormSubmit:
    def __init__(self, url):
        self.url = url

    def submit(self, name, drink):
        # Replace with actual entry IDs from your Google Form
        data = {
            "entry.557483856": name,  # Replace with the actual entry ID for the name field
            "entry.669075582": drink,  # Replace with the actual entry ID for the drink field
        }
        try:
            r = requests.post(self.url, data=data)
            r.raise_for_status()  # Raise an error for bad status codes
            print("Form submitted successfully.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return r.status_code

    def process_multiple_request_with_time(self, users, time_interval):
        for user in users:
            print("DATA", user)
            print(f"Submitting form for {user.get('nombre')} with drink {user.get('bebida')}...")
            self.submit(user.get("nombre"), user.get("bebida"))
            time.sleep(time_interval)
        return True
