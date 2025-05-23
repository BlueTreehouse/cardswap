import sys
import json
from formatter import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dict.py <path_to_decklist>")
        sys.exit(1)
    decklist_path = sys.argv[1]

    decklist = get_decklist(decklist_path)
    processed_decklist = category_remove(line_remove(line_split(decklist)))

    replacement_info = {}

    for line in processed_decklist:
        words = line.split()
        quantity = int(words[0])
        set_num = f"{words[-2]} {words[-1]}"
        card_name = " ".join(words[1:-2])

        if card_name not in replacement_info:
            replacement_info[card_name] = []
        replacement_info[card_name].append({
            "quantity": quantity,
            "set_num": set_num
        })

    print("Copy into Python dictionary")
    for key, value in replacement_info.items():
        print(f'    "{key}": [')
        for idx, item in enumerate(value):
            if idx == len(value) - 1:
                print(f'        {json.dumps(item, separators=(",", ": "))}')
            else:
                print(f'        {json.dumps(item, separators=(",", ": "))},')
        print(f"    ],")



    

def get_decklist(path):
    with open(path) as f:
        return f.read()
    
main()



