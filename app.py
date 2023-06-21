import csv
import datetime

CONTACTS_FILE = f"contactbook_{datetime.date.today().strftime('%d%m%Y')}.csv"

def create_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone_numbers = input("Enter phone numbers (comma-separated): ").split(",")
    address = input("Enter address: ")
    insertion_date = datetime.datetime.now()

    contact = [name, email, phone_numbers, address, insertion_date]

    with open(CONTACTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

    print("Contact saved successfully.")

def update_contact():
    contact_id = input("Enter contact ID to update: ")
    field = input("Enter field to update (name, email, phone_numbers, address): ")
    new_value = input("Enter new value: ")

    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if int(contact_id) <= len(contacts):
        contact = contacts[int(contact_id) - 1]
        if field in ['name', 'email', 'address']:
            contact[CONTACT_FIELDS.index(field)] = new_value
        elif field == 'phone_numbers':
            contact[CONTACT_FIELDS.index(field)] = new_value.split(",")
        else:
            print("Invalid field.")
            return

        with open(CONTACTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact updated successfully.")
    else:
        print("Invalid contact ID.")

def delete_contact():
    contact_id = input("Enter contact ID to delete: ")

    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if int(contact_id) <= len(contacts):
        contacts.pop(int(contact_id) - 1)

        with open(CONTACTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact deleted successfully.")
    else:
        print("Invalid contact ID.")

def list_contacts():
    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if len(contacts) > 0:
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact ID: {i}")
            print(f"Name: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone Numbers: {', '.join(contact[2])}")
            print(f"Address: {contact[3]}")
            print(f"Insertion Date: {contact[4]}\n")
    else:
        print("No contacts found.")

def main():
    while True:
        print("Contact Book")
        print("1. Create Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import csv
import datetime

CONTACTS_FILE = f"contactbook_{datetime.date.today().strftime('%d%m%Y')}.csv"

def create_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone_numbers = input("Enter phone numbers (comma-separated): ").split(",")
    address = input("Enter address: ")
    insertion_date = datetime.datetime.now()

    contact = [name, email, phone_numbers, address, insertion_date]

    with open(CONTACTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

    print("Contact saved successfully.")

def update_contact():
    contact_id = input("Enter contact ID to update: ")
    field = input("Enter field to update (name, email, phone_numbers, address): ")
    new_value = input("Enter new value: ")

    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if int(contact_id) <= len(contacts):
        contact = contacts[int(contact_id) - 1]
        if field in ['name', 'email', 'address']:
            contact[CONTACT_FIELDS.index(field)] = new_value
        elif field == 'phone_numbers':
            contact[CONTACT_FIELDS.index(field)] = new_value.split(",")
        else:
            print("Invalid field.")
            return

        with open(CONTACTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact updated successfully.")
    else:
        print("Invalid contact ID.")

def delete_contact():
    contact_id = input("Enter contact ID to delete: ")

    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if int(contact_id) <= len(contacts):
        contacts.pop(int(contact_id) - 1)

        with open(CONTACTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact deleted successfully.")
    else:
        print("Invalid contact ID.")

def list_contacts():
    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    if len(contacts) > 0:
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact ID: {i}")
            print(f"Name: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone Numbers: {', '.join(contact[2])}")
            print(f"Address: {contact[3]}")
            print(f"Insertion Date: {contact[4]}\n")
    else:
        print("No contacts found.")

def main():
    while True:
        print("Contact Book")
        print("1. Create Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
