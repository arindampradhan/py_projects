# recursive way of witing factorial
def fact( n ):
	if ( n == 0 ):
		return 1.0
	elif (n < 0):
		raise exception("Cannot calculate factorial of a negative number")
   	return fact( n - 1)*n;


if __name__ == "__main__":
	for i in range(0,10+1):
	    print "%d! = %g" %(i,fact(i))
	    print fact( -5 ) # clears the following