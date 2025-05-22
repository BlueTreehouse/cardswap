from replacer import *
from dictionaries.pokemon import pokemon
from dictionaries.trainers import trainers
from dictionaries.energy import energy

def main():
    decklist_path = "decklist/gardy.txt"
    decklist = get_book_text(decklist_path)
    split = line_split(decklist)
    remove_blank = line_remove(split)
    remove_cat = category_remove(remove_blank)
    
    replacement_info = {}
    for dict_to_merge in [pokemon, trainers, energy]:
        for card_name, replacements in dict_to_merge.items():
            if card_name not in replacement_info:
                replacement_info[card_name] = []
            replacement_info[card_name].extend(replacements)
    
    
    
    new_decklist = card_replacer(remove_cat, replacement_info)
   # print (remove_cat)

    print ("\n".join(new_decklist))

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()