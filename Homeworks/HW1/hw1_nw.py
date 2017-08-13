import random

class Portfolio():
	def __init__(self, treasury=0.00):
		self.treasury=treasury
		self.stock = {}
		self.ownedstock = {}
		self.mf = {}
		self.log = []
		trans="Portfolio created."
		self.track(trans)

	def track(self,transaction):
		print transaction
		self.log.append(transaction)

	def history(self):
		print 'Portfolio History:'
		for i in self.log:
			print i

	def __str__(self):
		return """Current balance is: $%.2f
You own the following stocks:\n%s
You own the following mutual funds:\n%s""" % (self.treasury,self.ownedstock,self.mf)

	def addCash(self,amount):
		self.treasury += amount
		trans = 'Added $%s to the portfolio. Balance is: $%.2f' % (amount, self.treasury)
		self.track(trans)

	def withdrawCash(self,amount):
		if self.treasury - amount < 0:
			return 'Not enough cash for this withdrawl.'
		else:
			self.treasury -= amount
			trans = 'Withdrew $%s cash from the portfolio. Balance is: $%.2f' % (amount, self.treasury)
			self.track(trans)

	def buyStock(self,shares,stock_name):
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
		if stock_name in self.ownedstock:
			if shares <= self.ownedstock[stock_name]:
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
		if type(shares)==float:
			if fund in self.mf:
				if shares <= self.mf[fund]:
					self.mf[fund] = round((self.mf[fund] - shares), 2)
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
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		print 'Created the stock %s with share price: $%s.' % (self.abbrev,self.price)


class MutualFund():
	def __init__(self,abbrev):
		self.price= 1
		self.abbrev=abbrev
		print 'Created the %s fund with share price: $%s.' % (self.abbrev,self.price)
