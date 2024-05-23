import easygui


while True:
    if easygui.ynbox("Hello!, Do You Want To View Instuctions Before Continuing\n"
                     "", choices=["Yes", "No"] ):
        easygui.msgbox("--- Welcome to the Monster Card Catalouge ---\n"
                       "-- This Program allows you to manage cards inside a catalogue --\n"
                       " You can Store cards, Add cards, Search For Cards, Edit Cards,\n"
                       "                                Delete Cards and Print Cards\n"
                       "\nYou will be prompted with a main menu that you will be able "
                       "                                to interact with\n"
                       "The cards consist of a name and 4 attributes\n"
                       "Strength, Speed, Stealth and Cunning\n"
                       "Which each go from 1-25"
                       "", "Instructions")
        break

    else:
        break