class Portfolio_year:
	"""
	This class calculates your IRA portfolio at an per year basis with varying 
	interest rates saving your accrued balance.
	
	Input:

	EX) Year1 = Portfolio_year(0) ==> starting balance
		Year1.balance(5500,0.11, 3) ==> adds interest to balance
		Year.current ==> access the balance in your account

	Output:
	Year1.current ==> current balance of your portfolio.
	Year1.contribution ==> the total number dollars contributed to the account.
	Year1.num_year_contributions ==> the number of contributions in total ex) 1 years = 1 , 2 years = 2


	Author: Alan Ly 10-31-18

	"""

	def __init__(self,current_balance):

		self.current_balance = current_balance							#current balance stored in IRA account
		self.prev_balance = 0
		self.contribution = 0
		self.num_year_contributions = 0		
		self.prev_num_year_contributions = 0
		self.interest_list = []

		#for plotting purposes
		self.list_dollars = []						

	def balance(self,contribution,interest,num_years):

		"""
			Updates your balance of your IRA account by the max amount of 5500 a year max
		"""

		while contribution >5500:
			contribution = int(input("Please enter amount less than 5500: "))

		self.prev_balance = self.current_balance 							   #save previous balance
		self.prev_num_year_contributions = self.num_year_contributions #save previous years contribution
		self.num_year_contributions += num_years 				#count the number of times balanced is invoked
		self.contribution = contribution*num_years 				#the total contributions you put into your account

		for year in range(0,num_years):

																#starting balance when you first open an ira account
			if year == 0 and self.current_balance == 0:
				self.current_balance = self.current_balance + contribution

																#start accrueing interest on your saved balance 
			else:
				self.current_balance = self.current_balance*interest + self.current_balance + contribution

			#add all current balances to the plot
			self.list_dollars.append(self.current_balance)
			self.interest_list.append(interest)

			#print(self.list_dollars)

		print(self.interest_list)
		print(self.current_balance)

	def withdraw(self,amt_withdrawl):

		"""
			Take an amount of money out of your current balance after 5 years has passed.
			There is overdraft protection.

		"""
																#if 5 year requirement is not met cannot withdraw
		if self.num_year_contributions < 5:						
			print("Cannot withdraw, 5 year requirement has not been met: %d years" %self.num_year_contributions)
			return False													
																#5 year requirement is met
		else:
			if self.current_balance - amt_withdrawl > 0:				#check if the withdrawl amount is less than your current balance
				self.prev_balance = self.current_balance
				self.current_balance -= amt_withdrawl
				print(self.current_balance)

				#add the balance from withdrawing to the plot
				self.list_dollars.append(self.current_balance)
				return True
			else:
				print("Sorry cannot withdrawl more than your account balance.")
				return False

	def clear(self):
		"""
			Resets all class variables of Portfolio_year

		"""
		self.current_balance = 0
		self.prev_balance = 0
		self.prev_num_year_contributions = 0
		self.num_year_contributions = 0

		#empties the list
		del self.list_dollars[:]


