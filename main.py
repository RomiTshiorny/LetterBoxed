import os
import csv

string = "CVOTNMPALIRE"
sides = [
    [string[0], string[1], string[2]],
    [string[3], string[4], string[5]],
    [string[6], string[7], string[8]],
    [string[9], string[10], string[11]]
]

box = f"  {sides[0][0]} {sides[0][1]} {sides[0][2]} " \
      f"\n{sides[1][0]}\t\t{sides[2][0]}" \
      f"\n{sides[1][1]}\t\t{sides[2][1]}" \
      f"\n{sides[1][2]}\t\t{sides[2][2]}" \
      f"\n  {sides[3][0]} {sides[3][1]} {sides[3][2]} "
print(box)


def isLegal(valid_chars, word):
    # Two 'illegal cases'
    # Case 1: Letters not part of the valid chars
    # Case 2: Adjacent letters never belong to the same 'side' of the box
    return False  # TODO Implement logic


def getLegalWords(valid_chars):
    directory = ".\\Words\\EOWL CSV Format"
    word_files = os.listdir(directory)
    legal_files = []
    legal_words = []
    for file in word_files:

        # All words are pre-sorted into files based on the letter they start with
        # Follows the name pattern 'X Words.csv' where X is the starting letter
        if valid_chars.__contains__(file[0]):
            legal_files.append(file)

    for file in legal_files:
        print(file)
        with open(f"{directory}\\{file}", mode='r') as text:
            try:
                words = csv.reader(text)
                for word in words:
                    if isLegal(word):
                        legal_words.append(word)
            finally:
                continue

    return legal_words


def run():
    legal_words = getLegalWords(string)
    print(legal_words)


run()
