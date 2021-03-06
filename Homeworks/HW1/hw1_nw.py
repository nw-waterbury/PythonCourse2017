#####################
####Homework 1
####Nick Waterbury
####Financial Script
#####################

#This program follows the template in the pdf. Assigned names are used to buy
#stocks and funds, while the string abbreviations are used to sell them


#Random needed for drawing from uniform distribution
import random

class Portfolio():
	"""10 function class that creates a portfolio and performs basic upkeep """
	def __init__(self, treasury=0.00):
		"""Set up for cash, stocks, mutual funds, and the log """
		self.treasury=treasury
		self.stock = {}
		self.ownedstock = {}
		self.mf = {}
		self.log = []
		trans="Portfolio created."
		self.track(trans)

	def track(self,transaction):
		"""Writes in the log, prints intermediate messages as updates """
		print transaction
		self.log.append(transaction)

	def history(self):
		"""Prints current log """
		print 'Portfolio History:'
		for i in self.log:
			print i

	def __str__(self):
		"""Prints portfolio's current cache of cash, stocks, and mutual funds"""
		return """Current balance is: $%.2f
You own the following stocks:\n%s
You own the following mutual funds:\n%s""" % (self.treasury,self.ownedstock,self.mf)

	def addCash(self,amount):
		"""Adds cash to the portfolio"""
		self.treasury += amount
		trans = 'Added $%s to the portfolio. Balance is: $%.2f' % (amount, self.treasury)
		self.track(trans)

	def withdrawCash(self,amount):
		"""Subtracts cash from the portfolio"""
		if self.treasury - amount < 0:
			return 'Not enough cash for this withdrawl.'
		else:
			self.treasury -= amount
			trans = 'Withdrew $%s cash from the portfolio. Balance is: $%.2f' % (amount, self.treasury)
			self.track(trans)

	def buyStock(self,shares,stock_name):
		"""Purchases existing stock with cash already in the portfolio"""
		if shares % 1 != 0:
			print "Stocks must be bought as whole shares. We will round down for you."
		if self.treasury < (float(stock_name.price)* int(shares)):
			return "Insufficient funds for this purchase"
		else:
			self.ownedstock[stock_name.abbrev] = shares
			self.stock[stock_name.abbrev] = stock_name.price
			self.treasury -= (stock_name.price * (shares))
			trans = "You bought %s shares of %s. Balance is: $%.2f." %(shares, stock_name.abbrev, self.treasury)
			self.track(trans)


	def sellStock(self,shares,stock_name):
		"""Sells stock in the portfolio for cash"""
		if stock_name in self.ownedstock:
			if shares <= self.ownedstock[stock_name]:
				#Price is determined by a random draw from unif. dist.
				price = (round(random.uniform(.5,1.5), 2) * self.stock[stock_name])
				self.treasury += (price * shares)
				self.ownedstock[stock_name] -= shares
				trans="You sold %s shares of %s at %s. Balance is: $%.2f." %(shares, stock_name, price, self.treasury)
				self.track(trans)
			else:
				return "Not enough shares of stock for this transaction."
		else:
			return "Portfolio does not contain any of this stock."

	def buyMutualFund(self,shares,fund):
		"""Purchases existing mutual funds with cash already in the portfolio"""
		if type(shares)==float:
			if self.treasury < shares:
				return "Insufficient funds for this purchase."
			else:
				self.mf[fund.abbrev] = shares
				self.treasury -= shares
				trans="You bought %s shares of %s. Balance is: $ %.2f." %(shares, fund.abbrev, self.treasury)
				self.track(trans)
		else:
			return "Mutual Funds must be bought as fractional shares."

	def sellMutualFund(self,shares,fund):
		"""Sells mutual funds in the portfolio for cash"""
		if type(shares)==float:
			if fund in self.mf:
				if shares <= self.mf[fund]:
					self.mf[fund] = round((self.mf[fund] - shares), 2)
					##Price is determined by a random draw from unif. dist.
					price = round(random.uniform(.9, 1.2), 2)
					self.treasury = self.treasury + (price * shares)
					trans = "You sold %s shares of %s at $ %s. You have now have $ %.2f." %(shares, fund, price, self.treasury)
					self.track(trans)
				else:
					return "Insufficient shares for this transaction."
			else:
				return "Portfolio does not contain any of this fund."
		else:
			return "Mutual Funds must be sold as fractional shares."


class Stock():
	"""Class Stock is a one function class that
	 creates a stock based on a given abbreviation and given price"""
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		print 'Created the stock %s with share price: $%s.' % (self.abbrev,self.price)


class MutualFund():
	"""Class MutualFund is a one function class that
	creates a mutual fund based on a given abbreviation and given price"""
	def __init__(self,abbrev):
		self.price= 1
		self.abbrev=abbrev
		print 'Created the %s fund with share price: $%s.' % (self.abbrev,self.price)
################################################################################
################################################################################
################################################################################
#Testing
portfolio = Portfolio()
portfolio.addCash(1300.50)
portfolio.withdrawCash(230)

s = Stock(25, "LLM")
s2 = Stock(10, "CBS")
mf1 = MutualFund("QRS")
mf2 = MutualFund("TUV")
mf3 = MutualFund("WXY")

print s2
print mf2

portfolio.buyStock(5, s)
portfolio.buyStock(2, s)
portfolio.buyStock(3, s2)
portfolio.buyMutualFund(8, mf1)
portfolio.buyMutualFund(4, mf2)
portfolio.buyMutualFund(5, mf2)


portfolio.sellStock(1, "LLM")
portfolio.sellMutualFund(1, "TUV")

## All of these throw errors as expected.
portfolio.sellStock(7, "CBS")
portfolio.sellStock(1.5, "CBS")
portfolio.sellStock(1.5, "CBC")
portfolio.buyStock(1000, s )
portfolio.sellMutualFund(1, "WXY")
portfolio.sellMutualFund(10, "TUV")

portfolio.history()
print portfolio
portfolio
