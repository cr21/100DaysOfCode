# List Implementation of Stack
class Stack:

    def __init__(self):
        self._stack = list()
        self.size = 0

    def  push(self,key):
        # last in first out
        # 10
        self._stack.append(key)
        self.size += 1

    def isEmpty(self):
        return  self.size == 0

    def top(self):
        if self.isEmpty()  :
            return None
        else:
            return self._stack[-1]

    def pop(self):
        if self.isEmpty():
            raise  Exception("Trying to pop from empty stack")
        else:
            _top = self.top()
            self._stack.pop()
            self.size -= 1
            return _top


__stack = Stack()
__stack.push(10)
__stack.push(100)
__stack.push(330)
print(__stack.top())
print(__stack.pop())
print(__stack.top())