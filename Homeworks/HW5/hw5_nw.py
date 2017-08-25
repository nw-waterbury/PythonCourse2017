#I am not very good at identifying complexity classes
#I assume the worst

class LinkedList():

	def __init__(self, value):
		self.head = Node(value)

	def length(self):
		"""Moves through the linked list, counting items until the last node """
		#Complexity class- n
		count = 1
		start = self.head
		while start.next != None:
			count += 1
			start = start.next
		return count

	def addNodeAfter(self, new_value, after_node):
		"""Creates a new node, adds it immediately after an existing node"""
		#Complexity class- n
		try:
			new_value=int(new_value)
			new_node=Node(new_value, after_node.next)
			after_node.next=new_node
			return new_node
		except: print "Invalid Input. Try again!"

	def addNode(self, new_value):
		"""Finds the end of the list, then adds a new node at that spot """
		#Complexity class- n
		try:
			new_value=int(new_value)
			new_node = Node(new_value)
			at_bat=self.head
			while at_bat.next != None:
				at_bat = at_bat.next
			at_bat.next
			return self.addNodeAfter(new_value, at_bat)
		except: print "Invalid Input. Try again!"

	def addNodeBefore(self, new_value, before_node):
		"""Finds the desired location in the list, then adds a new node """
		#Complexity class- n
		try:
			new_value=int(new_value)
			start = self.head
			while start.next != before_node:
				start = start.next
			return self.addNodeAfter(new_value, start)
		except: print "Invalid Input. Try again!"

	def removeNode(self, node_to_remove):
		"""Removes the desired node, go through the list moving all nodes up"""
		#Complexity class- n
		start = self.head
		while start.next != node_to_remove:
			start = start.next
		start.next = node_to_remove.next

	def removeNodesByValue(self, value):
		"""Removes all nodes with the value, moves other nodes up accordingly"""
		#Complexity class- n^2
		try:
			value=int(value)
			start = self.head
			while start.next != None:
				if start.value == value:
					self.removeNode(start)
				start = start.next
			if start.value == value:
				self.removeNode(start)
		except: print "Invalid Input. Try again!"

	def findNodeBefore(self, after_node, before = 'head'):
		"""Helper for reverse- finds the function immediately before an input"""
		if before == 'head': before = self.head
		if before.next == after_node: return before
		return self.findNodeBefore(after_node, before.next)

	def reverse(self):
		"""Moves through the list reversing the order of the nodes """
		#Complexity class- n
		leadoff = self.head
		while leadoff.next:
			leadoff = leadoff.next
		first = leadoff
		while leadoff != self.head:
			leadoff.next = self.findNodeBefore(leadoff)
			leadoff = leadoff.next
		self.head.next = None
		self.head = first
		return self

	def __str__(self):
		"""Prints an object of class LinkedList to like a traditional list"""
		#Complexity class- n
		node = self.head
		result = '['+str(node)
		while node.next:
			result += (', '+str(node.next))
			node = node.next
		return result + ']'

	def __repr__(self):
		"""Returns a call of a class LinkedList object just as in __str__"""
		#Complexity class- n
		return self.__str__()


class Node(object):
	def __init__(self, _value=None, _next=None):
		self.value=_value
		self.next=_next
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
###################################################################
###################################################################
###########################QUICK TESTS###################################
###################################################################
###################################################################
j=LinkedList(8)
print j
#8
##################################################################
node_7 = j.addNode(7)
node_5 = j.addNode(5)
j
#8,7,5
##################################################################
node_6 = j.addNodeBefore(6, node_7)
node_3 = j.addNodeAfter(3, node_5)
node_0 = j.addNodeAfter(0, node_3)
node_9 = j.addNodeAfter(9, node_0)
print j
#8,6,7,5,3,0,9
##################################################################
j.removeNode(node_3)
j.removeNodesByValue(5)
j
#8,6,7,0,9
##################################################################
j.reverse()
print j
#9,0,7,6,8
##################################################################
j.length()
#5
##################################################################
