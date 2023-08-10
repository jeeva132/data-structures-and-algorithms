class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.value = value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        return new_node
    
    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while(temp.next):
            pre= temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        self.value = value
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        temp = self.head
        newNode.next  = temp
        self.head = newNode
        self.length +=1
        return True
    
    def pop_first(self):
        if self.head is None:
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == None:
            self.head = None
            self.tail = None
        return temp

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast= fast.next.next
        return slow

    def display(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def get(self,index):
        
        temp = self.head
        i = 0
        while (temp.next):
            if i == index:
                return temp.value
            temp = temp.next
            i +=1

    def set(self,index,value):
        newNode = Node(value)
        if 1>index>self.length:
            return None
        temp = self.head
        prev = self.head
        i = 0
        while temp.next!=None:
            if i == index:
                prev.next = newNode
                newNode.next = temp
                return newNode
            prev = temp
            temp = temp.next
            i +=1
        temp.next = newNode
        newNode.next = None
        return temp


    def remove_duplicates(self):
        cur = self.head
        while cur:
            nextnode = cur.next
            if cur.value == nextnode.value:
                cur.next = nextnode.next
                nextnode.next = None
            print(cur.value)
            cur = cur.next
        return cur
newNode = LinkedList(40)
newNode.append(8634)
newNode.append(34)
newNode.append(34)
newNode.prepend(100)
newNode.append(20)
newNode.append(20)
newNode.prepend(100)
newNode.get(2)
newNode.set(3,130)
print(newNode.get_middle())
print(newNode.remove_duplicates())