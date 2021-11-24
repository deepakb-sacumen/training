class Queue:

    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to the front element in the queue
        self.rear = -1  # rear points to the last element in the queue
        self.count = 0  # current size of the queue

    def pop(self):
        if self.isEmpty():
            print("Queue Underflow!! Terminating process.")
            exit(1)

        print("Removing element ", self.q[self.front])

        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def append(self, value):
        if self.isFull():
            print("Overflow!! Terminating process.")
            exit(1)

        print("Inserting element…", value)

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating process.")
            exit(1)

        return self.q[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':

    # create a queue
    q = Queue(5)
    q.append(1)
    q.append(2)
    q.append(3)

    print("The queue size is", q.size())
    print("The front element is", q.peek())
    q.pop()
    print("The front element is", q.peek())

    q.pop()
    q.pop()

    if q.isEmpty():
        print("The queue is empty")
    else:
        print("The queue is not empty")