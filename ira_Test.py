from ira_calculations_class import Portfolio_year
import unittest

"""
	Test Cases to test the Portfolio_year class functions

	Author: Alan Ly 11-02-18
"""

class TestPortfolioClass(unittest.TestCase):

	#setUp is applied to all test cases in the TestPortfolioClass class
	def setUp(self):
		self.myPortfolio = Portfolio_year(0)

	def test_balance_one_year(self):
		self.myPortfolio.balance(5500,0.07,1)
		#assert statement is used to test the code
		self.assertEqual(self.myPortfolio.current_balance, 5500)

	def test_balance_multi_year(self):
		self.myPortfolio.balance(5500,0.07,10)
		self.assertEqual(int(self.myPortfolio.current_balance),75990)

	def test_clear(self):
		self.myPortfolio.balance(5500,0.07,1)
		self.myPortfolio.clear()
		self.assertEqual(self.myPortfolio.current_balance,0)

	def test_early_withdrawl(self):
		self.myPortfolio.balance(5500,0.07,1)
		self.assertTrue(self.myPortfolio.withdraw(5000) == False)

	def test_withdrawl(self):
		self.myPortfolio.balance(5500,0.07,5)
		self.assertTrue(self.myPortfolio.withdraw(5000) == True)

	def test_withdrawl_overdraft(self):
		self.myPortfolio.balance(5500,0.07,6)
		self.assertTrue(self.myPortfolio.withdraw(60000) == False)
	

	#after each test is ran clear the stored balance
	def tearDown(self):
		self.myPortfolio.clear()

# __name__ == '__main__' is applied when importing a module or class to another file
#this prevents the code outside of the TestPortfolioClass class to be ran when imported to another file
if __name__ == '__main__':
	unittest.main()