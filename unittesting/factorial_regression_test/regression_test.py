# Each test point lives in a function named as ‘test_’ 
# and it exercises the various cases of the ‘fact’ 
# and compares the results against the inbuilt math function 
# ‘math.factorial’. Usually the comparison of function 
# output with known results is done using the 
# unit-test API methods.




import unittest
import math
import factorial
from test import test_support

class FactorialTest(unittest.TestCase):
	def SetUp(self):
		print "setup"

	def tearDown(self):
		print "cleanup"

	def test_positives(self):
		for x in range(0,10+1):
			act = math.factorial(x)
			val = factorial.fact(x)
			print "%d! = %g == %g" %(x,val,act)
			self.assertAlmostEqual(act,val,1e-1)

	def test_negatives(self):
		passed = False
		# try:
		# 	factorial.fact(-3)
		# except Exception as e:
		# 	passed = True and (e.message.lower().find("cannot calculate"))>=0
		# self.assertTrue(passed)

		# alternate way
		with self.assertRaises(Exception) as cm:
			factorial.fact(-3)	

if __name__ == "__main__":
	test_support.run_unittest(FactorialTest)
