"""Implementation of Queue using a list"""
class QueueList:
    def __init__(self,li):
        self.li = []

    def isempty(self):
        """Queue is empty"""
        if not self.li:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def queue_length(self):
        """Check queue length"""
        self.size = int(input("Enter the size:"))
        print("Queue Length",self.size)

    def push(self,val):
        """Push an item in list"""
        i=0
        if val not in self.li:
            self.li.append(val)

        print("Push",val,"in queue")

    def dequeue(self):
        """Pop an item from list"""
        num = self.li.pop(0)
        print("Pop",num,"from queue")

    def printdisplay(self):
        print(self.li)

ql = QueueList(li=[])
ql.isempty()
ql.queue_length()
for i in range(ql.size):
    ql.push(int(input("Enter value to be inserted:")))
ql.printdisplay()
ql.dequeue()



