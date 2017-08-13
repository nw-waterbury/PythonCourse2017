from random import *

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
		return """Current balance is: $%.f
You own the following stocks:\n%s
You own the following mutual funds:\n%s""" % (self.treasury,self.ownedstock,self.mf)

	def addCash(self,amount):
		self.treasury += amount
		trans = 'Added $%s to the portfolio. Balance is: $%.f' % (amount, self.treasury)
		self.track(trans)

	def withdrawCash(self,amount):
		if self.treasury - amount < 0:
			print 'Not enough cash for this withdrawl.'
		else:
			self.treasury -= amount
			trans = 'Withdrew $%s cash from the portfolio. Balance is: $%.f' % (amount, self.treasury)
			self.track(trans)

	def buyStock(self,shares,stock_name):
		if self.treasury < (float(stock_name.price)* int(shares)):
			return "Insufficient funds for this purchase"
		else:
			self.ownedstock[stock_name.abbrev] = shares
			self.stock[stock_name.abbrev] = stock_name.price
			self.treasury -= (stock_name.price * (shares))
			trans = "You bought %s shares of %s. Balance is: $%.f." %(shares, stock_name.abbrev, self.treasury)
			self.track(trans)

	def sellStock(self,shares,stock):
		self.shares = int(shares)
		sale = self.shares * (uniform(0.5,1.5) * stock.price)
		if stock.abbrev in self.stock:
			if shares <= self.stock[stock.abbrev]:
				self.treasury += sale
				self.stocks[stock.abbrev] -= self.shares
				trans = 'Sold %s shares of %s stock.' % (self.shares, self.stock)
				self.track(trans)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (self.stocks[stock.abbrev],self.shares)
		else:
			print 'You do not own any of this stock.'

	def buyMutualFund(self,shares,fund):
		cost = shares * 1
		if self.treasury - cost >= 0:
			self.treasury -= cost
			self.mf[fund.abbrev] += shares
			x = 'Purchased %s shares of the %s fund.' % (shares,fund)
			self.track(x)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)

	def sellMutualFund(self,shares,fund):
		sale = shares * (uniform(0.9,1.2))
		if fund.abbrev in self.mf:
			if shares <= self.mf[fund.abbrev]:
				self.treasury += sale
				self.mf[fund.abbrev] -= shares
				x = 'Sold %s shares of the %s fund.' % (shares,fund)
				self.track(x)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (funds[fund.abbrev],shares)
		else:
			print 'This fund does not exist, or you typed the variable incorrectly.'



class Stock():
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		print 'Created the stock %s with share price: $%s.' % (self.abbrev,self.price)


class MutualFund():
	def __init__(self,abbrev):
		self.price= 1
		self.abbrev=abbrev
		Portfolio.mf[abbrev] = 0
		print 'Created the %s fund with share price: $%s.' % (self.abbrev,self.price)
