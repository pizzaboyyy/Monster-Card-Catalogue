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


def add_card():
    while True:
        add_card = easygui.multenterbox("Add Card\nCard attributes must be between 1-25",
                                        "Please Add New Card",
                                        ["Name", "Strength", "Speed", "Stealth", "Cunning"])

        if add_card is None:
            return

        card_name = add_card[0]
        try:
            card_attributes = list(map(int, add_card[1:]))
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

       



if 1 == 1:
    add_card()
    easygui.msgbox(cards_list)
