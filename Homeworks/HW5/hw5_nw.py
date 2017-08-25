class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.reverse = None

	def length(self):
		count = 1
		start = self.head_node
		while start.next != None:
			count += 1
			start = start.next
		return count

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

	def addNodeBefore(self, new_value, before_node):
		start = self.head
		while start.next != before_node:
			start = start.next
		return self.addNodeAfter(new_value, start)

	def removeNode(self, node_to_remove):
		start = self.head
		while start.next != node_to_remove:
			start = start.next
		start.next = node_to_remove.next

	def removeNodesByValue(self, value):
		start = self.head
		while start.next != None:
			if start.value == value:
				self.removeNode(start)
			start = start.next
		if start.value == value:
			self.removeNode(start)

	#def __str__(self):

	def __repr__(self):
		return self.__str__()

	class Node:
	  	def __init__(self, _value=None, _next=None):
		  	self.value=_value
		  	self.next=_next
		def __str__(self):
		  	return str(self.value)
