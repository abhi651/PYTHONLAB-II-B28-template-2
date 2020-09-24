import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def minimum(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        minimum_num = num1
    elif num2 < num1 and num2 < num3:
        minimum_num = num2
    else:
        minimum_num = num3
    return minimum_num        
       
   


# DO NOT TOUCH THE BELOW CODE
class TestMinimum(unittest.TestCase):

    def test_01(self):
        self.assertEqual(minimum(3,5,10), 3)

    def test_02(self):
        self.assertEqual(minimum(-3,5,10), -3)

    def test_03(self):
        self.assertEqual(minimum(-3,5,0), -3)


if __name__ == '__main__':
    unittest.main(verbosity=2)

