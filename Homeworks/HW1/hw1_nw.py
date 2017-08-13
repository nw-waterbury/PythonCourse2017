from random import *
stock={}
mf={}
log=[]
class Portfolio():
	def __init__(self, x=stock, y=mf, z=log):
		self.treasury=0.00
        self.stock=x
        self.mf=y
        self.log=z

	def track(self,transaction):
		print transaction
		log.append(transaction)

	def history(self):
		print 'Portfolio History:'
		for i in log:
			print i

	def __str__(self):
		return """Current balance is: $%.f
			   You own the following stocks:\n%s
You own the following mutual funds:\n%s""" % (self.treasury,self.stock,self.mf)

	def addCash(self,amount):
		self.treasury += amount
		trans = 'Added $%s to the portfolio' % (amount)
		self.track(trans)

	def withdrawCash(self,amount):
		if self.treasury - amount < 0:
			print 'Not enough cash for this withdrawl.'
		else:
			self.treasury -= amount
			trans = 'Withdrew $%s cash from the portfolio.' % (amount)
			self.track(trans)

	def buyStock(self,shares,stock):
		self.shares = int(shares)
		cost = self.shares * stock.price
		if self.treasury - cost >= 0:
			self.treasury -= cost
			stocks[stock.abbrev] += self.shares
			trans = 'Purchased %s shares of %s stock.' % (self.shares,stock)
			self.track(trans)
		else:
			print 'Not enough cash for this purchase. Balance is: $%s. Cost is: $%s.' % (self.treasury,cost)

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
		Portfolio.stocks[abbrev] = 0
		print 'Created the stock %s with share price: $%s.' % (self.abbrev,self.price)
	def __repr__(self):
		return self.abbrev

class MutualFund():
	def __init__(self,abbrev):
		self.price= 1
		self.abbrev=abbrev
		Portfolio.mf[abbrev] = 0
		print 'Created the %s fund with share price: $%s.' % (self.abbrev,self.price)
	def __repr__(self):
		return self.abbrev
