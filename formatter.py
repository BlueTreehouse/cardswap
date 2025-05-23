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

