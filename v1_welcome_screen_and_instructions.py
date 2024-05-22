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
                       "", "Instructions")
        break

    else:
        break