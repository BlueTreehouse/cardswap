import sys
from replacer import *
from formatter import *
from dictionaries.pokemon import pokemon
from dictionaries.trainers import trainers
from dictionaries.energy import energy

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    decklist_path = sys.argv[1]

    processed = category_remove(line_remove(line_split(get_decklist(decklist_path))))
    
    replacement_info = {}
    for dict_to_merge in [pokemon, trainers, energy]:
        for card_name, replacements in dict_to_merge.items():
            if card_name not in replacement_info:
                replacement_info[card_name] = []
            replacement_info[card_name].extend(replacements)
    
    new_list = card_replacer(processed, replacement_info)
    new_decklist = ("\n".join(new_list))

    print(f"PASTE THIS INTO PTCGL!!!\n{new_decklist}")

def get_decklist(path):
    with open(path) as f:
        return f.read()


main()