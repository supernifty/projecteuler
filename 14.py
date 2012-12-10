
answers = {}
answers[1] = 1

def chain(x):
  global answers
  if x in answers:
    return answers[x]
  if x % 2 == 0:
    result = 1 + chain(x/2)
  else:
    result = 1 + chain(x * 3 + 1)
  answers[x] = result
  return result
  
best = 0
best_x = -1
for x in xrange(1, 1000000):
  answers[x] = chain(x)
  if answers[x] > best:
    best_x = x
    best = answers[x]
    print best_x, best

print best_x, best
