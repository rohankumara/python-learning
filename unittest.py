import unittest

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
    
    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')