from Ans1 import Jumble
import unittest

class JumbleTests(unittest.TestCase):
	def testNormalInput(self):
		retString=Jumble("africa",1)
		self.assertTrue(retString)
		self.assertEqual(retString, "bgsjdb")
	def testCycling(self):
		retString=Jumble("xyza",3)
		self.assertTrue(retString)
		self.assertEqual(retString, "abcd")

		
	def testNumberTestZeroN(self):
		retString=Jumble("x1y2z3a4",0)
		self.assertTrue(retString)
		self.assertEqual(retString, "N should range between [1-1000]")


	def testNumberTestWithNString(self):
		retString=Jumble("x1y2m3a4",'10')
		self.assertTrue(retString)
		self.assertEqual(retString, "h1i2w3k4")


	def testSpecialCharsRemove(self):
		self.assertEqual(Jumble("red#bull&",29), "uhgexoo")


	def testNoCycleOnNzero(self):
		self.assertEqual(Jumble("sachin1",'wrongN'), "Wrong N: Integer required")


	def testCornerCaseN1000(self):
		str="kite"
		self.assertEqual(Jumble(str,1000), "wufq")


	def testCornerCaseN1001(self):
		str="kite"
		retString=Jumble(str,1001)
		self.assertTrue(retString)
		self.assertEqual(retString, "N should range between [1-1000]")


	def testNullString(self):
		string=None
		retString=Jumble(string,888)
		self.assertTrue(retString)
		self.assertEqual(retString, "Not a string")

if __name__ == '__main__':
	unittest.main()