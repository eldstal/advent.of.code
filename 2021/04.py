import aoc
import numpy as np
import colors

# Make another dutt on the bingo card
def dutt(numbers, dutts, call):
  dutts[numbers == call] = True
  return dutts

# Check if a card has a bingo
def has_bingo(dutts):
  row = np.any( [ np.all(dutts[r,:]) for r in range(5) ] )
  col = np.any( [ np.all(dutts[:,c]) for c in range(5) ] )
  return row or col

def card_score(numbers, dutts, call):
  total = np.sum(numbers[dutts == False])
  return total * call

def card_dump(numbers, dutts, call):
  for y in range(5):
    row = ""
    for x in range(5):
      text = f"{numbers[y,x]:4}"
      if numbers[y,x] == call:
        text = colors.green(text)
      elif dutts[y,x]:
        text = colors.red(text)
      row += text
    print(row)


DAY=4

_, lines = aoc.get_input(DAY)
_, lines = aoc.get_test_input(DAY)

# Each call is just a number
# Each card is a pair of (numbers, dutts)
calls = [ int(n) for n in lines[0].split(",") ]
cards = [ ]

# Parse bingo cards out of the remaining input
for start in range(1, len(lines), 5):
  card_data = lines[start:start+5]
  card_cells = [ [ int(n) for n in row.split() ] for row in card_data ]
  card_numbers = np.array(card_cells)
  card_dutts = np.full((5,5), False, dtype=bool)
  cards.append( (card_numbers, card_dutts) )


def find_winners(calls, cards):
  eliminated = [ ]
  scores = [ ]
  for call in calls:
    print(call)
    for i in range(len(cards)):
      if i in eliminated: continue

      numbers,dutts = cards[i]
      dutts = dutt(numbers, dutts, call)
      cards[i] = (numbers, dutts)

      if(has_bingo(dutts)):
        print("BINGO!")
        card_dump(numbers, dutts, call)

        eliminated.append(i)
        scores.append(card_score(numbers, dutts, call))

        if len(eliminated) == len(cards):
          return list(zip(scores, eliminated))

winners = find_winners(calls, cards)

answer_a = winners[0][0]
answer_b = winners[-1][0]


print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))

