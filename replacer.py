from quantities import rarity_dict

# Splits the decklist into a list of lines.
def line_split(decklist):
    lines = decklist.split("\n")
    return lines


# Removes empty lines.
def line_remove(decklist):
    new_list = []
    for line in decklist:
        if len(line) != 0:
            new_list.append(line)
    return new_list

# Removes the category lines.
def category_remove(decklist):
    new_list = []
    for line in decklist:
        if line[0].isdigit() == True:
            new_list.append(line)
    return new_list

#replacer for Arven.
def arven_replacer(decklist):
    new_decklist = []
    
    for line in decklist:
        words = line.split()
        if len(words) < 4:
            new_decklist.append(line)
            continue
        
        quantity = words[0]    # First element is the quantity of cards
        set_code_pos = -2      # Second to last element is set code
        collector_num_pos = -1 # Last element is collector number

        # everything between quantity and set code is the card name
        card_name = " ".join(words[1:set_code_pos])
    
        if card_name in rarity_dict:
            # Pull the information from the dictionary
            new_set_and_number = rarity_dict[card_name]
            # Create the new line: quantity + card name + new set info
            new_line = f"{quantity} {card_name} {new_set_and_number}"
            new_decklist.append(new_line)
                
        else:
            new_decklist.append(line)
            
    return new_decklist
