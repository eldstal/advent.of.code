import aoc

DAY=8

_, lines = aoc.get_input(DAY)
#_, lines = aoc.get_test_input(DAY)

inputs = []
for l in lines:
  noise = [ set(seq) for seq in l.split("|")[0].strip().split(" ") ]
  digits = [ set(seq) for seq in l.split("|")[1].strip().split(" ") ]

  inputs.append((noise, digits))

# These are the proper signal sets for each digit
CODES = {
  0: set("abcefg"),
  1: set("cf"),      # The only one with length 2
  2: set("acdeg"),
  3: set("acdfg"),
  4: set("bcdf"),    # The only one of length 4
  5: set("abdfg"),
  6: set("abdefg"),
  7: set("acf"),     # The only one of length 3
  8: set("abcdefg"), # The only one of length 7
  9: set("abcdfg")
}

answer_a = 0
for noise,digits in inputs:
  lengths = [ len(d) for d in digits ]
  answer_a += lengths.count(2)
  answer_a += lengths.count(4)
  answer_a += lengths.count(3)
  answer_a += lengths.count(7)

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))

def of_length(group, length):
  return [ x for x in group if len(x) == length ]

def unscramble(noise, riddle):

  # Scrambled segments that are known (key is the unscrambled segment name)
  segment = { }

  # Scrambled digits of known value (key is the numeric digit)
  digit = {}

  # 1, 4, 7 and 8 are easy to find
  digit[1] = of_length(noise, 2)[0]
  digit[4] = of_length(noise, 4)[0]
  digit[7] = of_length(noise, 3)[0]
  digit[8] = of_length(noise, 7)[0]

  # Whatever is in 7 but not 1 is seg a
  segment["a"] = digit[7] - digit[1]

  # 7 plus two more segments must be 3
  digit[3] = [ seq for seq in of_length(noise, 5) if digit[7].issubset(seq) ][0]

  # We can find segment d this way:
  segment["d"] = (digit[3] - digit[1]) & digit[4]

  # And by elimination, that gives us segment g as well
  segment["g"] = digit[3] - digit[7] - segment["d"]

  # Zero is the one missing only d
  digit[0] = digit[8] - segment["d"]

  # b is the only one in 4 but not 3
  segment["b"] = digit[4] - digit[3]

  # Number 5 is like 3, but with one segment moved to b
  digit[5] = [ seq for seq in of_length(noise, 5) if seq - digit[3] == segment["b"] ][0]

  # We're missing 2, 6 and 9. 2 is the last one of length 5.
  digit[2] = [ seq for seq in of_length(noise, 5) if seq not in [ digit[3], digit[5] ] ][0]

  # 2, 5 and 1 let us identify segment c, and therefore also segments f and e
  segment["c"] = digit[2] & digit[1]
  segment["f"] = digit[1] - digit[2]

  # Oh, hello
  digit[9] = digit[5] | segment["c"]
  digit[6] = digit[8] - segment["c"]

  # String up the sequence so it can be hashed
  key = { "".join(sorted(seq)): digit for digit,seq in digit.items() }

  # String up the digit so it can be joined
  answer = [ str(key["".join(sorted(seq))]) for seq in riddle ]

  # ...because the answer is a four-digit number. Of course.
  return int("".join(answer))

answer_b = 0
for noise,digits in inputs:
  answer = unscramble(noise, digits)
  answer_b += answer

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))
