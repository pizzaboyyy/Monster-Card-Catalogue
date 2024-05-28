import easygui

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

edit_card()



easygui.msgbox(cards_list)
