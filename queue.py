class Queue:
      
      def_init_(self):
	 self.items=[]
 	

	def enqueue(self,item):
	    self.items.append(item)
	def size(self):
	    return len(self.items)
	def is_empty(self):
	    return len(self.item_==0
	def dequeue(self):
	    if self.is_empty():
		return None
	    return self.items.pop(0)
	def peek(self):
	    if self.is_empty():
		return None
	    return self.items[0]
 
