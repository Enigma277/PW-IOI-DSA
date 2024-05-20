class Node :
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class Stack: 
    def __init__(self) -> None:
        self.head = None
        self.sz = 0
    
    def size(self) -> int :
        return self.sz
    
    def isEmpty(self) -> bool :
        return self.size() == 0
    
    def push(self, val) :
        self.head = Node(val, self.head)
        self.sz += 1
    
    def pop(self) :
        if self.isEmpty() :
            raise Exception("Stack  Underflow")
        data = self.head.data
        temp = self.head
        self.head = self.head.next
        del temp
        self.sz -= 1
        return data
    
    def top(self) :
        if self.isEmpty() :
            raise Exception("Stack Underflow")
        return self.head.data
    
    def __str__(self) :
        st = []

        trav = self.head
        while trav :
            st.append(str(trav.data))
            trav = trav.next

        return '->'.join(st)


#Test
st = Stack()
st.push(5)
st.push(10)

print(st)
print(st.size())
st.push(11)
st.push(13)
print(st)
print(st.pop())
print(st)
print(st.top())
print(st)