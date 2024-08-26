import os
from functools import reduce

string = "ANLRGDHWETIB"
sides = list(map(lambda index: string[index:index + int(len(string)/4)], range(0, len(string), int(len(string)/4))))
print(sides)

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
    directory = ".\\Words\\EOWL LF Delimited Format"
    word_files = os.listdir(directory)
    legal_files = []
    legal_words = {}
    for file in word_files:

        # All words are pre-sorted into files based on the letter they start with
        # Follows the name pattern 'X Words.txt' where X is the starting letter
        if valid_chars.__contains__(file[0]):
            legal_files.append(file)

    for file in legal_files:
        with open(f"{directory}\\{file}", mode='r', encoding="utf-8") as text:
            words = text.read().splitlines()
            for word in words:
                word_upper = word.upper()
                if isLegal(valid_sides, word_upper):
                    legal_words.update(
                        {word_upper[0]: [word_upper] + (legal_words.get(word_upper[0], []))}
                    )

    return legal_words


def run():
    legal_words = getLegalWords(sides)
    print(legal_words)


run()
