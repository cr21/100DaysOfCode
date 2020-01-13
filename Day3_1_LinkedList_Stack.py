class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList_Stack:
    def __init__(self):
        self.head = None
        self.size=0

    def pushFront(self,key):
        node = Node(key)
        if self.head is not None:
            currenthead = self.head
            node.next = currenthead
            self.head=node
        else:
            self.head = node
        self.size+=1


    def top_front(self):
        return self.head.value

    def pop_front(self):
        self.size += 1
        if self.head is not None:
            currenthead = self.head
            self.head = self.head.next
            return currenthead
        return None


    def length(self):
        return self.size

    def isEmpty(self):
        return  self.size  == 0


    def print_linkedList(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode= currentnode.next


stack = LinkedList_Stack()
stack.pushFront("a")
stack.pushFront("b")
stack.pushFront("d")
stack.pushFront("e")
stack.pushFront("f")

print(stack.pop_front().value)
print(stack.pop_front().value)
print(stack.pop_front().value)

stack.print_linkedList()
