class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.nodes = 1
		self.reverse = None
		self.cycle = False

	def length(self):
		return self.nodes

	def addNodeAfter(self, new_value, after_node):
		new_node=Node(new_value, after_node.next)
		after_node.next=new_node
		return new_node

	def addNode(self, new_value):
		new_node = Node(new_value)
		at_bat=self.head
		while at_bat.next != None:
			at_bat = at_bat.next
		at_bat.next
		return self.addNodeAfter(new_value, at_bat)

	def reverse(self):
		old_start=self.head
		new_start=self.reverse
		if old_start == None:
			self.head=self.reverse
			self.reverse=None
			print "The list has been reversed"
			return self

	def __str__(self):

	def __repr__(self):
		return self.__str__()

class Node:
  	def __init__(self, _value=None, _next=None):
	  	self.value=_value
	  	self.next=_next
	def __str__(self):
	  	return str(self.value)
