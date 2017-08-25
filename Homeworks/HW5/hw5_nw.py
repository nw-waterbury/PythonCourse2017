class LinkedList():

	def __init__(self, value):
		self.head = Node(value)


	def length(self):
		count = 1
		start = self.head
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


	def findNodeBefore(self, after_node, before = 'head'):
		if before == 'head': before = self.head
		if before.next == after_node: return before
		return self.findNodeBefore(after_node, before.next)

	def reverse(self):
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
		node = self.head
		result = '['+str(node)
		while node.next:
			result += (', '+str(node.next))
			node = node.next
		return result + ']'

	def __repr__(self):
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

node_7 = j.addNode(7)
node_5 = j.addNode(5)
j
#8,7,5

node_6 = j.addNodeBefore(6, node_7)
node_3 = j.addNodeAfter(3, node_5)
node_0 = j.addNodeAfter(0, node_3)
node_9 = j.addNodeAfter(9, node_0)
print j
#8,6,7,5,3,0,9

j.removeNode(node_3)
j.removeNodesByValue(5)
j
#8,6,7,0,9

j.reverse()
print j
#9,0,7,6,8

j.length()
#5
