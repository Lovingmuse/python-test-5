from solution import unittest
# Place your tests here
class TestProgrammer(unittest.TestCase):
  def setUp(self):
      self.programmer = Programmer()
  def test_zero(self):
    '''если делимое равно 0'''
      self.assertEqual(self.programmer.salary(0, 1),0)
  def test_normal(self):
    '''если числа обычные'''
      self.assertEqual(self.programmer.salary(2, 1), 2)

if __name__ == '__main__':
  unittest.main()
