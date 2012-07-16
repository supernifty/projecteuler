
s = 0
f0 = 1
f1 = 1
while True:
  n = f0 + f1
  if n > 4e6:
    break
  if n % 2 == 0:
    s += n
  f0 = f1
  f1 = n
print s
