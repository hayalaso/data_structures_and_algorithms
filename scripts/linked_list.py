
class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self,head=None):
        self.head=head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        i = 1
        while i < position:
            current = current.next
            i+=1
        if current:
          return current
        else: 
          return None

    def insert(self, new_element, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        """
        after_element = self.get_position(position)
        new_element.next = after_element

        if position == 1:
            pass
        else:
            before_element = self.get_position(position-1)
            before_element.next = new_element

    def delete(self,value):
        """
        Delete the first node with a given value.
        """
        current = self.head
        if current.value == value:
            self.head = current.next
            current.next = None
            pass
        
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                current.next.next = None  
                pass


    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self,new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


## Tests:

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)


print()
print("Stack")
# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)         
