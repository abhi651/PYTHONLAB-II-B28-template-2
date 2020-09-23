import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def swap(num1, num2):
    pass
    

# DO NOT TOUCH THE BELOW CODE
class TestSwap(unittest.TestCase):

    def test_01(self):
        self.assertEqual(swap(3,5), (5,3))

    def test_02(self):
        self.assertEqual(swap(19,-5), (-5,19))

    def test_03(self):
        self.assertEqual(swap(3,0), (0,3))

    def test_04(self):
        self.assertEqual(swap(300,5), (5,300))        
 
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
