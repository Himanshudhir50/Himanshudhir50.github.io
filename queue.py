class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('Hello')
    queue.enqueue('hi')
    queue.dequeue()
    print(queue.size())
