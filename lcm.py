import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def lcm(num1, num2):
    # Choose the greatest number
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while(True): 
        if greater % num1 == 0 and greater % num2 == 0:
            lcm_compute = greater
            break
        greater = greater + 1
    return lcm_compute 



# DO NOT TOUCH THE BELOW CODE
class TestLcm(unittest.TestCase):

    def test_01(self):
        self.assertEqual(lcm(3, 6), 6)

    def test_02(self):
        self.assertEqual(lcm(6, 10), 30)
    
    def test_03(self):
        self.assertEqual(lcm(6, 8), 24)  

if __name__ == '__main__':
    unittest.main(verbosity=2)          
