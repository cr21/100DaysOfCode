"""
Singly LinkedList implementation using Tail Pointer for better time complexity

for pushback and popback in O(1) times rather then O(N) times

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size=0

    def pushFront(self,key):
        node = Node(key)
        if self.head is not None:
            currenthead = self.head
            node.next = currenthead
            self.head=node
        else:
            self.head = node
        if self.tail is None:
            self.tail = self.head
        self.size+=1

    def pushBack(self,key):
        node = Node(key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else :
            currenttail = self.tail
            currenttail.next = node
            self.tail = node
        self.size += 1

    def popBack(self):
        head = self.head
        if self.tail is None:
            raise Exception ("trying to remove from the empty list")
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return head.value
        else :
            while head.next.next is not None:
                head = head.next
            self.tail = head
            popped =  head.next
            head.next = None
            self.size -= 1
            return popped.value



    def top_front(self):
        return self.head.value

    def pop_front(self):
        self.size -= 1
        head = self.head
        if self.tail is None :
            raise Exception("Trying to pop from empty list")
        if self.head ==  self.tail:
            self.head = None
            self.tail = None
            return head.value
        if self.head is not None:
            self.head = head.next
            return head.value


    def print_linkedList(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode= currentnode.next

    def length(self):
        return self.size

    def isEmpty(self):
        return  self.size  == 0


    def addAfter(self,_Node,key):
        node = Node(key)
        currentnode = self.head
        while currentnode:
            if currentnode.value == _Node:
                nextnode = currentnode.next
                currentnode.next = node
                node.next = nextnode
                return
            currentnode = currentnode.next


    def find(self,key):
        currentnode = self.head
        while currentnode:
            if currentnode.value == key:
                return True
            currentnode =  currentnode.next
        return False




    def addBefore(self,_Node,key):

        node = Node(key)
        currentnode = self.head
        if currentnode and _Node == currentnode.value:
            self.head = node
            node.next = currentnode
            return

        if currentnode.next is None:
            node.next = currentnode
            return

        while currentnode.next:
            # print("***")
            if currentnode.next.value == _Node:
                node.next = currentnode.next
                currentnode.next = node
                return
            currentnode =  currentnode.next

    def delete(self,key):
        currentnode = self.head
        if currentnode and currentnode.value == key:
            self.head = currentnode.next
            return
        while currentnode.next:
            if currentnode.next.value == key:
                foundednode =currentnode.next
                currentnode.next = foundednode.next
                return
            currentnode =  currentnode.next

ll = SinglyLinkedList()
ll.pushFront(7)

ll.pushFront(14)
ll.pushFront(102)
ll.pushBack(1000)

# print(ll.popBack())
# print(ll.pop_front())
# print(ll.popBack())
# print(ll.pop_front())
#
# print("**")
ll.print_linkedList()
# ll.popBack()
# ll.popBack()
# print("___")
# ll.print_linkedList()


