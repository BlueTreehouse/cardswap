def card_replacer(decklist, replacement_info):
    new_decklist = []
    
    for line in decklist:
        words = line.split()
        if len(words) < 4:  # Need at least quantity, name, set code, collector number
            new_decklist.append(line)
            continue
        
        try:
            quantity = int(words[0])  # First element is quantity (1-4)
        except ValueError:
            # If quantity can't be converted to int, skip this line
            new_decklist.append(line)
            continue
            
        card_name = " ".join(words[1:-2])  # Card name is between quantity and set code
        
        if card_name in replacement_info:
            replacements = replacement_info[card_name]
            remaining = quantity
            
            # If we don't have enough replacements, keep some original cards
            total_replacements = sum(rep['quantity'] for rep in replacements)
            if total_replacements < quantity:
                # Keep some original cards
                original_to_keep = quantity - total_replacements
                original_line = f"{original_to_keep} {' '.join(words[1:])}"
                new_decklist.append(original_line)
                remaining -= original_to_keep
            
            # Add each replacement
            for replacement in replacements:
                rep_quantity = min(replacement['quantity'], remaining)
                if rep_quantity <= 0:
                    continue
                    
                rep_set_num = replacement['set_num']
                rep_line = f"{rep_quantity} {card_name} {rep_set_num}"
                new_decklist.append(rep_line)
                remaining -= rep_quantity
                
                if remaining <= 0:
                    break
        else:
            # No replacement, keep original
            new_decklist.append(line)
    
    return new_decklist