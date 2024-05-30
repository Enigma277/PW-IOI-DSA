class Node:
    def __init__(self, data, next = None) :
        self.data = data
        self.next = next

class Queue :

    def __init__(self) :
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def size(self) :
        return self.__size
    
    def isEmpty(self) :
        return self.size() == 0

    def push(self, data) :
        newNode = Node(data)
        if(self.isEmpty()) :
            self.__head = self.__tail = newNode
        else :
            self.__tail.next = newNode
            self.__tail = newNode
        self.__size += 1

    def front(self) :
        if(self.isEmpty()) :
            raise Exception("Queue is Empty")
        else :
            return self.__head.data
    
    def pop(self) :
        if(self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            temp = self.__head
            self.__head = self.__head.next
            ret = temp.data
            del temp
            self.__size -= 1
            return ret
        
    def __str__(self):
        l = []
        trav = self.__head
        while trav is not None :
            l.append(str(trav.data))
            trav = trav.next
        return '->'.join(l)

#Test

q = Queue()

q.push(5)
q.push(10)
q.push(15)

print(q)
q.push(13)
print(q)
print(q.pop())
print(q)
print(q.front())
print(q)