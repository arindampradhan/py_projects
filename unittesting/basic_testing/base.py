#a test that fails
# it fails due to empty fixture

import unittest

class FooTests(unittest.TestCase):
    def testFoo(self):
        self.failUnless(False)

class DatePattern:
    def __init__(self,year,month,day):
        pass
    def matches(self,date):
        return True

def testMatches(self):
    p = DatePattern(2004,9,28)
    d = datetime.date(2004,9,28)
    self.failUnless(p.matches(d))




def main():
    unittest.main()

if __name__ == '__main__':
    main()

