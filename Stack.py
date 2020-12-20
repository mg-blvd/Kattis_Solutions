class Stack:
    #1. Initialize empty Stack
    def __init__(self):
        self.items = []

    #2. Check if stack is empty
    def isEmpty(self):
        return self.items == []

    #3. Push new items to the top of the Stack
    def push(self, data):
        self.items.append(data)

    #4 Popping data off of the Stack
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    #5. Returning size of the stack
    def size(self):
        return len(self.items)

    #6. Print the info
    def __repr__(self):
        return str(self.items)

    #7 Get top
    def get_top(self):
        return self.items[-1]

    #8 Get Second to top
    def get_second(self):
        return self.items[-2]

    #9 Return whole Stack
    def get_stack(self):
        return self.items
