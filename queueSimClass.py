
class QueueSimulator:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        self.rear += 1
        if self.rear == len(self.queue):
            self.queue.append(item)
        else:
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front > self.rear:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.front += 1
        return item

    def peek(self):
        if self.front > self.rear:
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    

    def printQueue(self):
        print("\n<--- FRONT-----------REAR--->\n")
        print('\nQueue: ', end="")
        for i in range(len(self.queue)):
            print(self.queue[i] + " ", end="")
        print()
    
    def isEmpty(self):
        return self.front > self.rear
    
    def isFull(self):
        return self.rear == len(self.queue) - 1
    

def main():
    queue = QueueSimulator()
    while True:
        print('\nEnter pq to print queue')
        print('Enter e to exit')
        print('Enter enqueue to enqueue data into queue')
        print('Enter dequeue to dequeue data from queue')
        print('Enter peek to peek at data from queue\n')
        command = input('Enter command: ')
        if command.lower() == 'pq':
            queue.printQueue()
        elif command.lower() == 'e':
            break
        elif command.lower() == 'enqueue':
            data = input('Enter data to enqueue: ')
            queue.enqueue(data)
        elif command.lower() == 'dequeue':
            try:
                data = queue.dequeue()
                print(f"Dequeued data: {data}")
            except IndexError as e:
                print(e)
        elif command.lower() == 'peek':
            try:
                data = queue.peek()
                print(f"Peeked data: {data}")
            except IndexError as e:
                print(e)
        else:
            print("Invalid command")

main()