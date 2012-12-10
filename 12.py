import math

def divisors( t ):
  m = int( math.sqrt( t ) )
  r = 0
  for p in xrange( 1, m+1 ):
    if t % p == 0:
      r += 2

  if m * m == t:
    r -= 1

  return r

i = 1
t = 0
best = 0

while True:
  t += i
  d = divisors( t )
  #print i, t, d
  #if i > 20:
  #  break
  if d > best:
    best = d
    print t, d, i
  if d > 500:
    print t
    break
  i += 1
