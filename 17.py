

m = { '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '1000': 'onethousand' }

def words(n):
  global m
  s = str(n)
  s = s.lstrip('0')
  if s in m:
    return m[s]
  if len(s) == 3:
    if s[1:] == '00':
      return m[s[0]] + "hundred"
    return m[s[0]] + "hundredand" + words(s[1:])  
  if len(s) == 2:
    return m[s[0] + '0'] + words(s[1:])

#print len(words(342))
#print len(words(115))

t = 0
for x in xrange(1, 1001):
  t += len(words(x))

print t
