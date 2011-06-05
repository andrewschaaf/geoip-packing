
import re
from itertools import islice


def uvarintEncode(x):
    bs = []
    while True:
        b = (x % 128) | (128 if x >= 128 else 0)
        bs.append(chr(b))
        
        if not (b & 128):
            return ''.join(bs)
        
        x = int(x / 128)


def uvarintWrite(f, x):
    f.write(uvarintEncode(x))


def freq(values):
  d = {}
  for x in values:
    d[x] = d.get(x, 0) + 1
  return d


def freqSorted(values):
  d = freq(values)
  for item in sorted(d.items(), lambda x, y: -cmp(x[1], y[1])):
    yield item


def parsedLines():
  with open("geoip.txt", "rb") as f:
    for line in f:
      m = re.search(r'^([0-9]+),([0-9]+),([A-Z]+)', line)
      if m:
        x1 = int(m.group(1))
        x2 = int(m.group(2))
        cc = m.group(3)
        yield x1, x2, cc


#                       (size)
# 0, 99 (DNE)           100
# 100,200,TESTING       101
# 201, 16777215 (DNE)   16777015
# 16777216,16777471,AU  256
def runSizes():
  last_x2 = -1
  for x1, x2, cc in parsedLines():
    if (last_x2 + 1) == x1:
      yield x2 - x1 + 1, cc
    else:
      yield x1 - last_x2 - 1, ""
      yield x2 - x1 + 1, cc
    last_x2 = x2


if __name__ == '__main__':
  pos = 0
  for (size, cc) in islice(runSizes(), 5):
    print pos, pos + size - 1
    pos += size

