#!/usr/bin/python
import time

prime = 5
divs = [3]
primes = [3,5]

ticks = time.time()


while prime < 99999:
	prime +=2
	divs.append(prime-2)
	for i in divs:
		a = prime % i
		#print prime, " mod ", i, " equals ", a
		if prime % i == 0:
			break
	else:
		#print prime, " is prime"
		primes.append(prime)
print primes
ticksf = time.time()

time=ticksf-ticks
print "It took ", time, "seconds to calculate this list of primes"
record = reduce(lambda x, y: x*y, primes)
print record
print "prime number", record-2
print "number of digits: ", len(str(record))
print "length of list: ", len(primes)