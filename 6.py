
sum_of_squares = 0
square_of_sums = 0

for i in xrange(1,101):
  sum_of_squares += i ** 2
  square_of_sums += i

square_of_sums = square_of_sums ** 2
print sum_of_squares, square_of_sums, square_of_sums - sum_of_squares
