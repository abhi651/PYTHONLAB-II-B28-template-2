import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def prime(num):
    pass
        

# DO NOT TOUCH THE BELOW CODE
class TestPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(prime(1000), False)

    def test_02(self):
        self.assertEqual(prime(6), False)

    def test_03(self):
        self.assertEqual(prime(-28), False)
    
    def test_04(self):
        self.assertEqual(prime(97), True)

    def test_05(self):
        self.assertEqual(prime(877), True)    


if __name__ == '__main__':
    unittest.main(verbosity=2)
