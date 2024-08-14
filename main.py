import enchant

# help(enchant)
enchant.list_dicts()

sides = [['C', 'V', 'O'], ['T', 'N', 'M'], ['P', 'A', 'L'], ['I', 'R', 'E']]
box = f"  {sides[0][0]} {sides[0][1]} {sides[0][2]} " \
      f"\n{sides[1][0]}\t\t{sides[2][0]}" \
      f"\n{sides[1][1]}\t\t{sides[2][1]}" \
      f"\n{sides[1][2]}\t\t{sides[2][2]}" \
      f"\n  {sides[3][0]} {sides[3][1]} {sides[3][2]} "
print(box)


def getNextOption(side):
    return None
