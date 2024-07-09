import pandas as pd
import os

# Define the CSV file path
csv_file = 'contacts.csv'

# Define the Contact class
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Function to read contacts from the CSV file
def read_contacts():
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame(columns=['Name', 'Phone', 'Email', 'Address'])

# Function to write contacts to the CSV file
def write_contacts(df):
    df.to_csv(csv_file, index=False)
