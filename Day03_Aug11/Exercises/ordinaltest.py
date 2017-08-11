import unittest
import ordinal_nw

class OrdinalTest(unittest.TestCase):

  def setup(self):
    pass

  def test_zero(self):
    self.assertEqual("0th", ordinal_nw.ordinal(0))

  def test_first(self):
    self.assertEqual("1st", ordinal_nw.ordinal(1))

  def test_second(self):
    self.assertEqual("2nd", ordinal_nw.ordinal(2))

  def test_third(self):
    self.assertEqual("3rd", ordinal_nw.ordinal(3))

  def test_fourth(self):
    self.assertEqual("4th", ordinal_nw.ordinal(4))

  def test_tenth(self):
    self.assertEqual("10th", ordinal_nw.ordinal(10))

  def test_one_hundred_twenty_three(self):
      self.assertEqual("123rd", ordinal_nw.ordinal(123))
if __name__=='__main__':
    unittest.main()
