import easygui

# List of all cards
cards_list = {
    "Stoneling": [
        ["Strength", 7],
        ["Speed", 1],
        ["Stealth", 25],
        ["Cunning", 15],
    ],
    "Vexscream": [
        ["Strength", 1],
        ["Speed", 6],
        ["Stealth", 21],
        ["Cunning", 19],
    ],
    "Dawnmirage": [
        ["Strength", 5],
        ["Speed", 15],
        ["Stealth", 18],
        ["Cunning", 22]
    ],
    "Blazegolem": [
        ["Strength", 15],
        ["Speed", 20],
        ["Stealth", 23],
        ["Cunning", 6]
    ],
    "Websnake": [
        ["Strength", 7],
        ["Speed", 15],
        ["Stealth", 10],
        ["Cunning", 5]
    ],
    "Moldvine": [
        ["Strength", 21],
        ["Speed", 18],
        ["Stealth", 14],
        ["Cunning", 5]
    ],
    "Vortexwing": [
        ["Strength", 19],
        ["Speed", 13],
        ["Stealth", 19],
        ["Cunning", 2]
    ],
    "Rotthing": [
        ["Strength", 16],
        ["Speed", 7],
        ["Stealth", 4],
        ["Cunning", 12]
    ],
    "Froststep": [
        ["Strength", 14],
        ["Speed", 14],
        ["Stealth", 17],
        ["Cunning", 4]
    ],
    "Wispghoul": [
        ["Strength", 17],
        ["Speed", 19],
        ["Stealth", 3],
        ["Cunning", 2]
    ]
}


def search_card():
    # enterbox to search for cards
    search_name = easygui.enterbox("Enter the name of the card to search\n"
                                   "    *Make Sure To Spell Card Right*\n"
                                   "          *Capital Letters Matter*", "Search Card")
    # Finding search for card
    if search_name:
        if search_name in cards_list:
            card_details = cards_list[search_name]
            find_card = f"Card: {search_name}\n\nAttributes:\n"
            for attribute in card_details:
                find_card += f"{attribute[0]}: {attribute[1]}\n"
            easygui.msgbox(find_card, "Card Details")
        # if card not found says to check card name
        else:
            easygui.msgbox(f"                                   Card '{search_name}' not found\n"
                           f"Please Make Sure You Entered The Card Name Correctly")
    else:
        easygui.msgbox("Nothing Entered.")


# Function to add cards
def add_card():
    while True:
        # Asks for card name and attribues
        add_cardd = easygui.multenterbox("Add Card\nCard attributes must be between 1-25\n",
                                         "Please Add New Card",
                                         ["Name", "Strength", "Speed", "Stealth", "Cunning"])

        if add_cardd is None:
            return

        card_name = add_cardd[0]
        # Checks card attribuetes to see if between 1 and 25
        try:
            card_attributes = list(map(int, add_cardd[1:]))
            if any(attr < 1 or attr > 25 for attr in card_attributes):
                easygui.msgbox("Attributes Have To Be Between 1 And 25, Try again", "Error")
                continue
        except ValueError:
            easygui.msgbox("Please enter valid numbers for the attributes", "Error")
            continue

        card_details = (f"Name: {card_name}\n"
                        f"Strength: {card_attributes[0]}\n"
                        f"Speed: {card_attributes[1]}\n"
                        f"Stealth: {card_attributes[2]}\n"
                        f"Cunning: {card_attributes[3]}")
        # Card Confirmation
        confirm = easygui.ynbox(f"Please confirm the card details:\n\n{card_details}", "Confirm Card Details")
        if confirm:
            cards_list[card_name] = [
                ["Strength", card_attributes[0]],
                ["Speed", card_attributes[1]],
                ["Stealth", card_attributes[2]],
                ["Cunning", card_attributes[3]]
            ]
            easygui.msgbox("Card added successfully", "Card Added")
            break
        else:
            easygui.msgbox("Card details not confirmed please re enter the details", "re-enter details")


# Function to print cards
def print_cards():
    message = ""
    # Makes name appear once and attribues appear below
    for card, attributes in cards_list.items():
        message += f"{card}:\n"
        for attribute in attributes:
            message += f"{attribute[0]}: {attribute[1]} "
        message += "\n"
        message += "-------------------------------------------------------------------------"
        message += "\n"
# prints cards
    easygui.msgbox(message, title="Cards list")


def edit_card():
    # Prompt the user to enter the name of the card to search for
    search_name = easygui.enterbox("Enter the name of the card to search\n"
                                   "*Make Sure To Spell Card Right*\n"
                                   "*Capital Letters Matter*")
    if search_name:
        # Check if the card exists
        if search_name in cards_list:
            card_details = cards_list[search_name]
            find_card = f"Card: {search_name}\n\nAttributes:\n"
            for attribute in card_details:
                find_card += f"{attribute[0]}: {attribute[1]}\n"
            easygui.msgbox(find_card, "Card Details")

            # Ask if the user wants to edit the card
            if easygui.ynbox("Do you want to edit this card?", choices=["Yes", "No"]):
                field_names = ["Card Name", "Strength", "Speed", "Stealth", "Cunning"]
                current_value = [search_name] + [str(attr[1]) for attr in card_details]
                new_values = easygui.multenterbox("Edit card Attributes\nAttributes must be between 1-25",
                                                  "Edit Card",
                                                  field_names, current_value)

                if new_values:
                    new_name = new_values[0]
                    new_attributes = new_values[1:]
                    try:
                        new_attributes = [int(value) for value in new_attributes]
                        if all(1 <= value <= 25 for value in new_attributes):
                            if new_name != search_name and new_name in cards_list:
                                easygui.msgbox("A card with the new name already exists. No changes were made.",
                                               "Error")
                                # removes card name and adds new name and attributes
                            else:
                                cards_list.pop(search_name)
                                cards_list[new_name] = [[field_names[i], new_attributes[i - 1]] for i in range(1, 5)]
                                easygui.msgbox("Card updated successfully", "Card updated")
                        # error messages
                        else:
                            easygui.msgbox("Attributes must be between 1 and 25. No changes were made.", "Error")
                    except ValueError:
                        easygui.msgbox("Invalid input. Attributes must be numbers. No changes were made.", "Error")
                else:
                    easygui.msgbox("No changes were made.")
        else:
            easygui.msgbox(f"Card '{search_name}' not found.")
    else:
        easygui.msgbox("Nothing entered.")


# Delete function
def delete_card():
    choices = list(cards_list.keys())
    selected_card = easygui.choicebox("Please select a card to delete:", "Delete Card", choices=choices)

    if selected_card:
        confirmation = easygui.ynbox(f"Are you sure you want to delete '{selected_card}'?", "Confirmation")
        if confirmation:
            # deletes card
            del cards_list[selected_card]
            easygui.msgbox(f"Card '{selected_card}' deleted successfully.", "Success")
            # Cancels deletion
        else:
            easygui.msgbox("Deletion canceled.", "Information")
            # If nothing entered it will say nothing entered
    else:
        easygui.msgbox("No card selected for deletion.", "Information")


# Function to print instructions if user needs
def instructions():
    easygui.msgbox(
        "                 --- Welcome to the Monster Card Catalogue ---\n"
        "-- This Program allows you to manage cards inside a catalogue --\n"
        "-- You can Store cards, Add cards, Search For Cards, Edit Cards--,\n"
        "--                                Delete Cards and Print Cards--\n"
        "\n--You will be prompted with a main menu that you will be able\n"
        "to interact with--\n"
        "--The cards consist of a name and 4 attributes--\n"
        "                               --Strength, Speed, Stealth and Cunning--\n"
        "                               --Which each go from 1-25--",
        "Instructions"
    )


# Ask if the user wants to view instructions before the main loop
view_instructions = easygui.ynbox("Do you want to view the instructions first?", "Instructions",
                                  choices=["Yes", "No"])
if view_instructions:
    instructions()

# Main loop
while True:
    action = easygui.buttonbox("What do you want to do?", "Choose an action",
                               choices=["Add", "Print", "Delete", "Edit", "Search", "Exit"])

    if action == "Search":
        search_card()
    elif action == "Print":
        print_cards()
    elif action == "Edit":
        edit_card()
    elif action == "Delete":
        delete_card()
    elif action == "Add":
        add_card()
    elif action == "Exit":
        break  # Exit the loop
