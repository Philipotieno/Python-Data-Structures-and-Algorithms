class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # checks of stck is empty

        # return len(self.items) == 0
        return not self.items

    def push(self, item):  # adds an item to a  stack
        self.items.append(item)

    def pop(self):  # retrieve item from the top of the stcack
        return self.items.pop()

    def peek(self):  # returns the last item in the list
        return self.items[-1]

    def size(self):  # returns size of the list
        return len(self.items)

    def __str__(
            self):  # enables the print statement to shpw what is in the Stack
        return str(self.items)


# s = Stack()
# print(s)
# print(s.is_empty())
# s.push(3)
# print(s)
# s.push("philip")
# s.push(55)
# print(s)
# print(s.pop())
# print(s)
# print(s.peek())
# print(s.size())
