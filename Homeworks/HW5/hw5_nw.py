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


	def findNodeBefore(self, after_node, before = 'start'):
		if before == 'start': before = self.start
		if before.next == after_node: return before
		return self.findNodeBefore(after_node, before.next)

	def reverse(self):
		leadoff = self.start
		while leadoff.next:
			leadoff = leadoff.next
		first = leadoff
		while leadoff != self.start:
			leadoff.next = self.findNodeBefore(leadoff)
			leadoff = leadoff.next
		self.start.next = None
		self.start = first
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

	class Node:
		def __init__(self, _value=None, _next=None):
			  self.value=_value
			  self.next=_next
		def __str__(self):
			  return str(self.value)
###################################################################
###################################################################
###########################TEST###################################
###################################################################
###################################################################
j=LinkedList(8)
print j

node_7 = l.addNode(7)
node_5 = l.addNode(5)
j

node_6 = l.addNodeBefore(6, node_7)
node_3 = l.addNodeAfter(3, node_5)
node_0 = l.addNodeAfter(0, node_3)
node_9 = l.addNodeAfter(9, node_0)
print j

j.remove(node_3)
j.removeNodesByValue(5)
j

j.reverse()
print j
