import os

myStack = ['', '', '']
topPointer = -1         # Create pointer and stack
def push(data):
    global topPointer
    if topPointer == len(myStack) - 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Overflow')
        return
    else:
        topPointer += 1
        myStack[topPointer] = data
def pop():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Underflow\n')
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        topPointer -= 1
        myStack[topPointer + 1] = ''
        return myStack[topPointer + 1]
def peek():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack Underflow\n')
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(myStack[topPointer])

def printStack():
    global topPointer
    if topPointer == -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stack is empty\n')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n<--- BOTTOM-----------TOP--->\n")
        print('\nStack: ', end="")
        for i in range(len(myStack)):
            print(myStack[i] + " ", end="")
        print()

def main():
    while True:
        print('\nEnter ps to print stack')
        print('Enter e to exit')
        print('Enter push to push data into stack')
        print('Enter pop to pop data from stack')
        print('Enter peek to peek at data from stack\n')

        command = input('Enter command: ')
        if command.lower() == 'ps':
            os.system('cls' if os.name == 'nt' else 'clear')
            printStack()
        elif command.lower() == 'e':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif command.lower() == 'push':
            os.system('cls' if os.name == 'nt' else 'clear')
            data = input('Enter data to push: ')
            push(data)
            print(data + ' added to stack\n')
        elif command.lower() == 'pop':
            os.system('cls' if os.name == 'nt' else 'clear')
            pop()
        elif command.lower() == 'peek':
            os.system('cls' if os.name == 'nt' else 'clear')
            peek()
main()
