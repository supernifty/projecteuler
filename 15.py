import math

def choose(n,k):
  return math.factorial(n) / math.factorial(k) / math.factorial(n-k)

n = 20

total = 0
for x in xrange(0, n+1):
  total += choose(n, x) ** 2

print n, total
