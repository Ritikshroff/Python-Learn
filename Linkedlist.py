class Rode:
    def __init__(self, info , next = None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self , head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Rode(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insetAtbeggening(self, value):
        temp = Rode(value)
        temp.next = self.head
        self.head = temp

    def insetinmiddle(self, value, location):
        temp = Rode(value)
        t1 = self.head

        while (t1.next != None):
            if(t1.data == location):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def delete(self, value):
        t1 = self.head
        prev = t1
        while (t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
                # t1.next = None
            else:
                prev = t1
                t1 = t1.next    

    def printLinklist(self):
        t1 = self.head
        while (t1 != None):
            print(t1.data)
            t1 = t1.next




obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.insetAtbeggening(5)
obj.insetinmiddle(25, 10)
obj.delete(25)
obj.printLinklist()