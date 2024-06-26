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
    search_name = easygui.enterbox("Enter the name of the card to search\n"
                                   "*Make Sure To Spell Card Right*\n"
                                   "*Capital Letters Matter*")
    if search_name:
        if search_name in cards_list:
            card_details = cards_list[search_name]
            find_card = f"Card: {search_name}\n\nAttributes:\n"
            for attribute in card_details:
                find_card += f"{attribute[0]}: {attribute[1]}\n"
            easygui.msgbox(find_card, "Card Details")
            if easygui.ynbox("Do you want to edit card", choices=["Yes", "No"]):
                                    easygui.multenterbox("Add Card\nCard attributes must be between 1-25",
                                    "Please Add New Card",
                                    ["Name", "Strength", "Speed", "Stealth", "Cunning"])



        else:
            easygui.msgbox(f"card '{search_name}' not found.")
    else:
        easygui.msgbox("Nothing Entered.")

edit_card()

