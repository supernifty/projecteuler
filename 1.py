# sum of integers < 1000 that are multiples of 3 or 5
s = 0
for x in xrange(1,1000):
  if x % 3 == 0 or x % 5 == 0:
    s += x
print s
