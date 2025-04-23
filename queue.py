class Queue:
      
      def_init_(self):
	 self.items=[]
 	

	def enqueue(self,item):
	    self.items.append(item)
	def size(self):
	    return len(self.items) 
