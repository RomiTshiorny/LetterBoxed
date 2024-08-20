import os
import csv
from functools import reduce

string = "CVOTNMPALIRE"
sides = list(map(lambda index: string[index:index + 3], range(0, len(string), 3)))

box = f"  {sides[0][0]} {sides[0][1]} {sides[0][2]} " \
      f"\n{sides[1][0]}\t\t{sides[2][0]}" \
      f"\n{sides[1][1]}\t\t{sides[2][1]}" \
      f"\n{sides[1][2]}\t\t{sides[2][2]}" \
      f"\n  {sides[3][0]} {sides[3][1]} {sides[3][2]} "
print(box)


def isLegal(valid_sides, word_to_check):
    
    # Three 'illegal cases'
    # Case 1: Word is 3 letters or shorter
    if len(word_to_check) <= 3:
        return False

    # Case 2: Letters not part of the valid chars
    valid_chars = ''.join(valid_sides)
    for char in word_to_check:
        if char not in valid_chars:
            return False

    # Case 3: Adjacent letters never belong to the same 'side' of the box
    chars = {}
    for c in word_to_check:
        for group in valid_sides:
            if c in group:
                chars.update({group: chars.get(group, 0) + 1})
                if chars.get(group, 0) > 1:
                    return False
            else:
                chars.update({group: 0})

    return True


def getLegalWords(valid_sides):
    valid_chars = ''.join(valid_sides)
    directory = ".\\Words\\EOWL CSV Format"
    word_files = os.listdir(directory)
    legal_files = []
    legal_words = []
    count = 0
    for file in word_files:

        # All words are pre-sorted into files based on the letter they start with
        # Follows the name pattern 'X Words.csv' where X is the starting letter
        if valid_chars.__contains__(file[0]):
            legal_files.append(file)

    for file in legal_files:
        with open(f"{directory}\\{file}", mode='r') as text:
            try:
                words = csv.reader(text)
                for word in words:
                    count += 1
                    if isLegal(valid_sides, word[0].upper()):
                        legal_words.append(word[0].upper())
            finally:
                continue

    print(f"Narrowed down {count} words to {len(legal_words)} legal words")
    return legal_words


def run():
    legal_words = getLegalWords(sides)
    print(legal_words)
    print(len(legal_words))


run()
