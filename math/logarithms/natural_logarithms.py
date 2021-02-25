import math
log = math.log

# math.log(x[, base])
# With one argument, return the natural logarithm of x (to base e).
# With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

# Base e (Euler’s number) is about 2.71828, of the parameter value (numeric expression), passed to it.
# e = lim(1 + 1 / n ) ** n ~= 2.71828
# n = 1000 -> 2.71692
# n = 10000 -> 2.71815
# n = 100000 -> 2.71827

# log e x -> ln x

log(2.71828) # == 1
# log e e == 1

# Any number to the power of zero equals 1
log(1) 
# log(1) == 0
# 2.71828 ** 0 == 1

# log e 5 -> ln5
log(5) 
# log(5) == 1.6094379124341003
# 2.71828 ** 1.6094379124341003 == 5

log(9)
# log(9) == 2.1972245773362196
# 2.71828 ** 2.1972245773362196 == 5
