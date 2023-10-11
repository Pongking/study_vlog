class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,data):
        self.head=ListNode(0)
        curr=self.head
        for i in range(data):
            node=ListNode(data[i])
            curr.next=node
            curr=curr.next
    def length(self):
        count=0
        curr=self.head
        while curr:
            count+=1
            curr=curr.next
        return count
    def find(self,val):
        curr=self.head
        while curr:
            if curr.val==val:
                return curr
            curr=curr.next
        return None
    def insertFront(self,val):
        tmp=ListNode(val)
        tmp.next=self.head
        self.head=tmp
    