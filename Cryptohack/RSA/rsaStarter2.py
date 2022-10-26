M = 12 # the message
e = 65537 #expoemt
q = 23 # prime 1
p = 17 # prime 2
n = p*q # product of two primes



x = pow(M, e, n)

print (x)

# The pow() function returns the value of x to the power of y (xy).
# If a third parameter is present, it returns x to the power of y, modulus z.
#
# Syntax: pow(x, y, z)
#
# Parameter	& Description
# x	= A number, the base
# y	= A number, the exponent
# z	= Optional. A number, the modulus
#
# reference: https://www.w3schools.com/python/ref_func_pow.asp