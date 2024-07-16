class Entry :
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __str__(self) :
        return str(self.key) + " : " + str(self.value)

class HT:
    def __init__(self) :
        self.size = 0
        self.capacity = 5
        self.data = [ [] for i in range(self.capacity)]

    def getSize(self) : 
        return self.size;

    def insert(self, key, value) :
        entry = Entry(key, value)
        index = entry.hash % self.capacity

        print ("inserting key : " + str(key) + " at index : " + str(index))
        isUpdated = False

        for i in range(len(self.data[index])) :
            if(self.data[index][i].key == key) :
                self.data[index][i] = entry
                isUpdated = True
                break
        
        if isUpdated == False :
            self.data[index].append(entry)
            self.size += 1
        



    def remove (self , key) :
        index = hash(key) % self.capacity

        for i in range(len(self.data[index])) :
            if(self.data[index][i].key == key) :
                del self.data[index][i]
                self.size -= 1
                break
        

    def get(self, key) :
        index = hash(key) % self.capacity
        
        for i in range(len(self.data[index])) :
            if(self.data[index][i].key == key) :
                return self.data[index][i].value
        
        return None

    def print(self) :
        for i in range(self.capacity) :
            print("bucket : " + str(i) + " : ")
            for e in self.data[i] :
                print(e, sep = "->")
        print("-------------")
    
####################################

hashTable = HT()

hashTable.insert("roll no 1", 123)
hashTable.insert("roll no 2", 112)

hashTable.print()

hashTable.remove("roll no 1")
hashTable.print()

hashTable.remove("roll no 7")
hashTable.print()
