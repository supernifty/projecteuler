
# a, b, c s.t. a^2 + b^2 = c^2 and a+b+c=1000

for a in xrange(1,1000):
  for b in xrange(1,1000):
    c = 1000 - a - b
    if c > 0 and c ** 2 == a ** 2 + b ** 2:
      print a, b, c
