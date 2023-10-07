import csv
import re

class Customer:
    def __init__(self, title, first_name, last_name, email, phone, address, blacklisted):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.blacklisted = blacklisted

    def __str__(self):
        return f"Customer: {self.title} {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Blacklisted: {self.blacklisted}"

class CustomerNotAllowedException(Exception):
    pass

def read_customer_data(filename):
    customers = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
        
            name_parts = re.match(r'(\w+)\. (\w+)\s+(\w+)', row['Name'])
            title, first_name, last_name = name_parts.groups() if name_parts else ('', '', '')
            customer = Customer(title, first_name, last_name, row['Email'], row['Phone'], row['Address'], int(row['Blacklisted']))
            customers.append(customer)
    return customers

fairdeal_customers = read_customer_data('FairDealCustomerData.csv')

for customer in fairdeal_customers:
    print(customer)
