# Have you ever been annoyed at having to change all the rarities of cards when you import a decklist from Limitless to PTCGL? Well, I made this tool to take a dictionary of cards that I have, and format a decklist copied from Limitless with those cards.

# This project would be unnecessary if either limitless had a way to keep track of which cards you own on ptcgl OR if the devs at PTCGL just implemented a "maximise rarity" button or something.

# To swap the card printings, save the decklist you want to convert into the "resources" folder. Open Console and type "python3 main.py resources/'decklist.txt'". Copy the newly formatted decklist and export it into PTCGL.


# To add to dictionary, export cards you own from PTCGL by adding them to a deck and then exporting the decklist. Save that to a text file and put it into the "resources" folder. Type the command "python3 dict.py resources/'decklist.txt'". Copy the outputted text into the appropriate dictionary in the "dictionaries" directory.