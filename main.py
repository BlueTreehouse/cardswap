from replacer import *

def main():
    decklist_path = "decklist/gardy.txt"
    decklist = get_book_text(decklist_path)
    split = line_split(decklist)
    remove_blank = line_remove(split)
    remove_cat = category_remove(remove_blank)

   # print (remove_cat)

    print (arven_replacer(remove_cat))

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()