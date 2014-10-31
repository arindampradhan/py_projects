# recursive way of witing factorial
def fact( n ):
	if ( n == 0 ):
		return 1.0
   	return fact( n - 1)*n;


if __name__ == "__main__":
	for i in range(0,10+1):
	    print "%d! = %g" %(i,fact(i))
	    fact( -5 ) #this causes an exception 

