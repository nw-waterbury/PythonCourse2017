import unittest
import lab3_nw

class LabTest(unittest.TestCase):


	def test_on_shout(self):
		self.assertEqual(lab3_nw.shout("hello"), "HELLO!")

	def test_on_reverse(self):
		self.assertEqual("elttiL", lab3_nw.reverse("Little"))
		self.assertRaises(SyntaxError, lab3_nw.reverse("bit louder"))
		self.assertEqual("!woN", lab3_nw.reverse("Now!"))


	def test_on_reverse_words(self):
		self.assertEqual("little A", lab3_nw.reversewords("A little"))
		self.assertEqual("louder bit", lab3_nw.reversewords("bit louder"))
		self.assertEqual("little A now", lab3_nw.reversewords("now A little"))


	def test_on_reverse_letter_and_word(self):
		self.assertEqual("elttil A", lab3_nw.reversewordletters("A little"))
		self.assertEqual("reduol tib", lab3_nw.reversewordletters("bit louder"))
		self.assertEqual("!won reduol tib elttil A !woN", lab3_nw.reversewordletters("Now! A little bit louder now!"))


	def test_pig_latin(self):
		self.assertEqual("oorday", lab3_nw.piglatin("door"))
		self.assertEqual("igpay", lab3_nw.piglatin("pig"))
		self.assertEqual("ichiganMay tateSay ocksray", lab3_nw.piglatin("Michigan State rocks"))


if __name__ == '__main__':
		unittest.main()
