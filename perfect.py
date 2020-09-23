import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def perfect(num):
    pass       
   


# DO NOT TOUCH THE BELOW CODE
class TestPerfect(unittest.TestCase):

    def test_01(self):
        self.assertEqual(perfect(3), False)

    def test_02(self):
        self.assertEqual(perfect(6), True)

    def test_03(self):
        self.assertEqual(perfect(28), True)
    
    def test_04(self):
        self.assertEqual(perfect(496), True)

    def test_05(self):
        self.assertEqual(perfect(8128), True)    


if __name__ == '__main__':
    unittest.main(verbosity=2)
