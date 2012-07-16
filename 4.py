
# abc * def = 123456
def is_palindrome(z):
  return z / 100000 == z % 10 and ( z / 10 ) % 10 == ( z / 10000 ) % 10 and ( z / 100 ) % 10 == ( z / 1000 ) % 10
  #return z / 1000 == z % 10 and ( z / 10 ) % 10 == ( z / 100 ) % 10

best = 0
for x in xrange(999,1,-1):
  for y in xrange(999,1,-1):
    z = x * y
    if z > best and is_palindrome(z):
      best = z
      print best, x, y
