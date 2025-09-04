import json
import os

from colorama import Fore, init

init(autoreset=True)

FILE_NAME = "contacts.json"


def notify(message: str, type: str = "info"):
    """
    Prints a message to the console with color coding based on the type and clears the screen first.

    Args:
        message (str): The message to be printed.
        type (str, optional): The type of message, which determines the color:
            - "success" -> green
            - "error"   -> red
            - "warning" -> yellow
            - "info"    -> default terminal color
            Defaults to "info".

    Example:
        notify("Operation completed successfully", type="success")
        notify("An error occurred!", type="error")
    """
    clear_screen()
    if type == "success":
        print(Fore.GREEN + message)
    elif type == "error":
        print(Fore.RED + message)
    elif type == "warning":
        print(Fore.YELLOW + message)
    else:
        print(message)


def clear_screen():
    """
    Clears the console screen depending on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def back_menu(user_input: str) -> bool:
    """
    Checks if the user input is a command to go back to the menu.

    Args:
        user_input (str): The user's text input.

    Returns:
        bool: True if the input is 'menu' (case-insensitive), False otherwise.
    """
    return user_input.lower() == "menu"


def load_contacts() -> dict[str, str]:
    """
    Loads contacts from the JSON file.

    Returns:
        dict[str, str]: A dictionary containing contacts as {name: phone_number}.
                        Returns an empty dictionary if the file does not exist.
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts: dict[str, str]):
    """
    Saves contacts to the JSON file.

    Args:
        contacts (dict[str, str]): The contacts dictionary to save.
    """
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def number_validation(number: str) -> bool:
    """
    Validates a phone number input.

    Args:
        number (str): The phone number entered by the user.

    Returns:
        bool: True if the number is valid (digits only or starts with '+'), False otherwise.
              Prints an error message if invalid.
    """
    number = number.strip()
    if back_menu(number):
        return False
    if number.isdigit() or (number.startswith("+") and number[1:].isdigit()):
        return True
    notify("Please enter a valid phone number", type="error")
    return False


def add_contact(contacts: dict[str, str]):
    """
    Adds a new contact to the contacts dictionary and saves it.

    Prompts the user for a contact name and phone number. Validates the input and updates the
    contacts dictionary. The 'menu' command can be used to cancel.

    Args:
        contacts (dict[str, str]): The contacts dictionary to update.
    """
    name = input("Contact name: ").strip()
    if back_menu(name):
        return

    while True:
        phone = input("Contact number: ").strip()
        if number_validation(phone):
            break

    contacts[name] = phone
    notify(f"Contact '{name}: {phone}' added.", type="success")
    save_contacts(contacts)


def delete_contact(contacts: dict[str, str]):
    """
    Deletes a contact from the contacts dictionary and saves the file.

    Args:
        contacts (dict[str, str]): The contacts dictionary to update.
    """
    while True:
        name = input("Contact name to delete: ").strip()
        if back_menu(name):
            return
        if name in contacts:
            del contacts[name]
            notify(f"Contact '{name}' deleted.", type="success")
            break
        else:
            print(f"Contact '{name}' not found.")
    save_contacts(contacts)


def search_contact(contacts: dict[str, str]) -> str | None:
    """
    Searches for a contact by name.

    Args:
        contacts (dict[str, str]): The contacts dictionary to search.

    Returns:
        str | None: The name of the found contact, or None if not found or canceled.
    """
    while True:
        name = input("Contact name: ").strip()
        if back_menu(name):
            return None
        if name in contacts:
            notify(f"{name}: {contacts[name]}")
            return name
        else:
            print(f"Contact '{name}' not found.")


def show_contacts(contacts: dict[str, str]):
    """
    Displays all contacts in alphabetical order.

    Args:
        contacts (dict[str, str]): The contacts dictionary to display.
    """
    clear_screen()
    if not contacts:
        print("No contacts found.")
        return
    print("Contacts:\n")
    for i, name in enumerate(sorted(contacts), start=1):
        print(f"{i} - {name}: {contacts[name]}")


def edit_contact(contacts: dict[str, str]):
    """
    Edits an existing contact's name or phone number.

    Args:
        contacts (dict[str, str]): The contacts dictionary to update.
    """

    contact_name = search_contact(contacts)
    if not contact_name:
        return

    while True:
        print("Do you want to change:\n 1. Name\n 2. Number")
        try:
            option = int(input("Option: "))
        except ValueError:
            notify("Please enter a valid number.", type="error")
            continue

        if option == 1:
            new_name = input("Enter new name: ").strip()
            contacts[new_name] = contacts.pop(contact_name)
            save_contacts(contacts)
            notify(f"Contact name changed to '{new_name}'.", type="success")
            break
        elif option == 2:
            while True:
                number = input("Enter new phone number: ").strip()
                if number_validation(number):
                    break
            contacts[contact_name] = number
            save_contacts(contacts)
            notify(f"Contact number updated for '{contact_name}'.", type="success")
            break
        else:
            notify("Please enter a valid option.", type="error")


def main():
    """
    Main function to run the contact manager menu.

    Handles user input and calls appropriate functions for adding, deleting, searching,
    showing, and editing contacts.
    """
    clear_screen()
    contacts = load_contacts()

    while True:
        print("\n--- Contact List ---")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Show all contacts")
        print("5. Edit contact")
        print("6. Exit")
        print("-- Enter 'menu' at any prompt to return to menu --")

        try:
            choice = int(input("Your choice: "))
        except ValueError:
            notify("Enter the number corresponding to each option.", type="error")
            continue

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            delete_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            show_contacts(contacts)
        elif choice == 5:
            edit_contact(contacts)
        elif choice == 6:
            save_contacts(contacts)
            notify("Exited the contact manager.", type="success")
            break
        else:
            notify("Enter a valid option.", type="error")


if __name__ == "__main__":
    main()
