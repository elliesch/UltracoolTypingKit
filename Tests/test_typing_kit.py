import unittest
from TypeFinder import *

class TestData(unittest.TestCase):

    def setUp(self):
    	'''
    	This defines data to test
    	'''
        self.data = Data('some_test_file')

    def test_init(self):
    	'''
    	This tests that the J-H-K arrays have been sorted properly by checking their boundary conds.
    	'''

        self.assertTrue([ii >= 0.87 and ii <= 1.39 for ii in self.data.wavelength_J])
        self.assertTrue([ii >= 1.41 and ii <= 1.89 for ii in self.data.wavelength_H])
        self.assertTrue([ii >= 1.91 and ii <= 2.39 for ii in self.data.wavelength_K])


### FUTURE TESTS ###
# 1. Test that the x-axis boundaries are logical on input data for J-H-K bands using get_axis
# 2. Test that pressing a letter key returns the proper error
# 3. Test that a png shows up when the correct key is pressed