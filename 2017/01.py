import aoc

data,_ = aoc.get_input(day=1, year=2017)

data = data.strip()

total = 0
for i in range(-1, len(data)-1):
  if data[i] == data[i+1]:
    total += int(data[i])

success,msg = aoc.post_result(day=1, part=1, value=total, year=2017)
print(success, msg)
