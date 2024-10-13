class Phonebook:
    def __init__(self):
        """Initialize the phonebook as an empty list."""
        self.phonebook = []

    def create_contact(self, name, phone):
        """Create a contact dictionary with name and phone."""
        return {"name": name, "phone": phone}

    def insert_contact(self, name, phone):
        """Insert a new contact into the phonebook."""
        contact = self.create_contact(name, phone)  # Create a new contact
        self.phonebook.append(contact)               # Add the contact to the phonebook
        return "Contact added successfully"          # Return success message

    def search_contact(self, query):
        """Search for a contact by name or phone number."""
        for contact in self.phonebook:               # Loop through each contact in the phonebook
            if contact["name"] == query or contact["phone"] == query:
                return contact                        # Return the contact if found
        return "Contact not found"                    # If no match is found, return a message

    def display_all_contacts(self):
        """Display all contacts in the phonebook."""
        if not self.phonebook:                       # Check if the phonebook is empty
            print("No contacts available")           # Notify if there are no contacts
        else:
            for contact in self.phonebook:            # Loop through and display each contact's details
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def delete_contact(self, query):
        """Delete a contact by name or phone number."""
        for contact in self.phonebook:               # Loop through each contact in the phonebook
            if contact["name"] == query or contact["phone"] == query:
                self.phonebook.remove(contact)       # Remove the contact if found
                return "Contact deleted"              # Confirm deletion
        return "Contact not found"                    # If no match is found, return a message

    def update_contact(self, query, new_name, new_phone):
        """Update the details of an existing contact."""
        for contact in self.phonebook:               # Loop through each contact in the phonebook
            if contact["name"] == query or contact["phone"] == query:
                contact["name"] = new_name           # Update the contact's name
                contact["phone"] = new_phone         # Update the contact's phone number
                return "Contact updated"              # Confirm update
        return "Contact not found"                    # If no match is found, return a message

    def sort_contacts(self):
        """Sort the contacts in the phonebook by name."""
        self.phonebook.sort(key=lambda contact: contact["name"])  # Sort the phonebook list
        return "Contacts sorted"                           # Confirm sorting

    def main(self):
        """Main function to display the phonebook menu and handle user input."""
        while True:
            # Display the phonebook menu options
            print("\nPhonebook Menu:")
            print("1. Insert Contact")
            print("2. Search Contact")
            print("3. Display All Contacts")
            print("4. Delete Contact")
            print("5. Update Contact")
            print("6. Sort Contacts")
            print("7. Exit")

            choice = input("Enter your choice: ")  # Get user input for the menu choice
            
            # Call the appropriate function based on user input
            if choice == "1":
                name = input("Enter name: ")         # Get name input
                phone = input("Enter phone: ")       # Get phone input
                print(self.insert_contact(name, phone))  # Insert contact and print result
            elif choice == "2":
                query = input("Enter name or phone to search: ")  # Get search query
                print(self.search_contact(query))            # Search contact and print result
            elif choice == "3":
                self.display_all_contacts()                  # Display all contacts
            elif choice == "4":
                query = input("Enter name or phone to delete: ")  # Get query for deletion
                print(self.delete_contact(query))            # Delete contact and print result
            elif choice == "5":
                query = input("Enter name or phone to update: ")  # Get query for update
                new_name = input("Enter new name: ")        # Get new name input
                new_phone = input("Enter new phone: ")      # Get new phone input
                print(self.update_contact(query, new_name, new_phone))  # Update contact and print result
            elif choice == "6":
                print(self.sort_contacts())                   # Sort contacts and print result
            elif choice == "7":
                print("Exiting Phonebook...")                # Exit message
                break                                          # Exit the loop and end the program
            else:
                print("Invalid choice, please try again.")  # Notify if the choice is invalid

# Entry point of the program
if __name__ == "__main__":
    phonebook_app = Phonebook()  # Create an instance of the Phonebook class
    phonebook_app.main()          # Call the main function to run the application
