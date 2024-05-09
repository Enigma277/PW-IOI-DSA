
class Node:
  ''' 
    Node class to represent data
  '''
  def __init__(self, data, prev=None, next=None): 
    self.data = data
    self.prev = prev
    self.next = next


class DoublyLinkedList: 
      
  def __init__(self): 
    self.__size = 0 
    self.__head = None
    self.__tail = None
    self.__iter = None
    
  def __len__(self): 
    """ 
    Return number of elements stored in array 
    """
    return self.__size


  def clear(self):
    return None

  def size(self):
    """ 
    Return the size of this linked list
    """
    return self.__size


  def isEmpty(self):
    """ 
    Is this linked list empty? 
    """
    return self.size() == 0


  def append(self, elem):
    """ 
    Add an element to the tail of the linked list, O(1)
    """
    if self.isEmpty() :
      self.__head = self.__tail = Node(elem, None, None)
    else :
      self.__tail.next = Node(elem, self.__tail, None)
      self.__tail = self.__tail.next
    self.__size += 1

  def addLast(self, elem):
    """ 
    Add a node to the tail of the linked list, O(1) 
    """
    self.append(elem)

  def addFirst(self, elem):
    """ 
    Add an element to the beginning of this linked list, O(1) 
    """
    if self.isEmpty() :
      self.__head = self.__tail = Node(elem, None, None)
    else :
      self.__head.prev = Node(elem, None, self.__head)
      self.__head = self.__head.prev
    self.__size += 1

  def addAt(self, index, data):
    """ 
    Add an element at a specified index
    """
    if index < 0 :
      raise Exception('index should not be negative. The value of index was: {}'.format(index))
    
    if index > self.size() :
      raise Exception('index should not be greater than size of the list')
    
    if index == 0 :
      self.addFirst(data)
      return
    
    if index == self.size() :
        self.addLast(data)
        return
      
    trav = self.__head
    for _ in range(0, index-1) :
      trav = trav.next
    
    newNode = Node(data, trav, trav.next)

    trav.next.prev = newNode
    trav.next = newNode

    self.__size += 1

  def peekFirst(self):
    """ 
    Check the value of the first node if it exists, O(1)
    """ 
    if self.isEmpty() :
      raise Exception('Empty List')
    
    return self.__head.data


  def peekLast(self):
    """ 
    Check the value of the last node if it exists, O(1)
    """ 
    if self.isEmpty() :
      raise Exception('Empty List')
    
    return self.__tail.data


  def removeFirst(self):
    """ 
    Remove the first value at the head of the linked list, O(1)
    """ 
    if self.isEmpty() :
      raise Exception('Empty List')
    
    self.__head =  self.__head.next
    self.__size -= 1

    if self.isEmpty() :
      self.__tail = None
    else :
      self.__head.prev = None

  def removeLast(self):
    """ 
    Remove the last value at the tail of the linked list, O(1)
    """ 
    if self.isEmpty() :
      raise Exception('Empty List')
    
    self.__tail = self.__tail.prev
    self.__size -= 1

    if self.isEmpty() :
      self.__head = None
    else :
      self.__tail.next = None

  def __remove__(self, node):
    """ 
    Remove an arbitrary node from the linked list, O(1)
    """ 
    if node.prev == None :
        self.removeFirst()
        return
    
    if node.next == None :
        self.removeLast()
        return
    
    node.prev.next = node.next
    node.next.prev = node.prev
    del node
    self.__size -= 1
    return None


  def removeAt(self, index):
    """ 
    Remove a node at a particular index, O(n)
    """ 
    if index < 0 or index >= self.__size :
      raise Exception("Invalid index")
    
    trav = self.__head
    i = 0
    while i != index :
      trav = trav.next
      i += 1

    return self.__remove__(trav)



  def indexOf(self, data):
    """ 
    Find the index of a particular value in the linked list, O(n)
    """ 
    trav = self.__head
    index = 0

    while trav is not None :
      if trav.data == data :
        return index
      
      index += 1
      trav = trav.next

    return -1


  def contains(self, data):
    """ 
    Check if a value is contained within the linked list
    """ 
    return self.indexOf(data) != -1


  def clear(self) :
    """
    Empty the Linked List
    """
    pass

  def __iter__(self): 
    self.__iter = self.__head
    return self


  def __next__(self): 
    if self.__iter is None :
        raise StopIteration
    
    data = self.__iter.data
    self.__iter = self.__iter.next
    return data


  def __str__(self):
    l = []
    trav = self.__head
    while trav is not None:
      l.append(trav.data)
      trav = trav.next
    return '<->'.join(map(str, l))


#Test the code
node = Node(5, None, None)
l = DoublyLinkedList()
print(node.data)
print(len(l))
print(l.size())
print(l.isEmpty())
l.append(5)
print(l.size())
l.addLast(10)
print(l)
l.addFirst(6)
print(l)
l.addAt(1, 15)
print(l)
l.removeAt(2)
print(l)
print(l.indexOf(10))
print(l.contains(15))
print(l.contains(19))