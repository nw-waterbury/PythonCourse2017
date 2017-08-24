import unittest
from hw4_nw import *

class SortTest(unittest.TestCase):

    def test_selectionSort(self):
        self.assertEqual(selectionSort([8,6,7,5,3,0,9]), [0,3,5,6,7,8,9])
    def test_insertionSort(self):
        self.assertEqual(insertionSort([8,6,7,5,3,0,9]), [0,3,5,6,7,8,9])
    def test_bubbleSort(self):
        self.assertEqual(insertionSort([8,6,7,5,3,0,9]), [0,3,5,6,7,8,9])

if __name__ == '__main__':
        unittest.main()
