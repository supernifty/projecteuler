l = (20,19,18,17,16,15,14,13,12,11,)

p = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2

def is_divisible(i):
  for j in l:
    if i % j != 0:
      return False
  return True

i = p
print p
while True:
  if is_divisible(i):
    print i
    break
  else:
    i += p

