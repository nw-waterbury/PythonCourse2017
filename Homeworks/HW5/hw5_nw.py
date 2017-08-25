class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.size = 1
		self.rev = None
		self.cycle = False

class Node:
  def __init
