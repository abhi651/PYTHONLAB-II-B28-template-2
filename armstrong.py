import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# Check whether the given number is Armstrong number or not 

def armstrong(num): 
    pass


# DO NOT TOUCH THE BELOW CODE
class TestArmstrong(unittest.TestCase):

    def test_01(self):
        self.assertEqual(armstrong(153), True)

    def test_02(self):
        self.assertEqual(armstrong(121), False)

    def test_03(self):
        self.assertEqual(armstrong(1253), False)
    
    def test_04(self):
        self.assertEqual(armstrong(407), True)

    def test_05(self):
        self.assertEqual(armstrong(8128), False)    


if __name__ == '__main__':
    unittest.main(verbosity=2)

          