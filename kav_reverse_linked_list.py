# Algorithm: To reverse the LinkedList
# 1. Keep 2 pointers prev = None, current pointing to head
# 2. Iterate through while until current is not None:
    # 3. store the current.next link 
    # 4. point the current.next to prev
    # 5. point the prev to the current
    # 6. move the current to the current.next whixh is stored in nxt
# 7. finally make last element where the prev as the head



class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def insert(self, val):
        # node = ListNode(val)
        if self.head is None:
            self.head = node
            return
        
        currentnode = self.head 
        while True:
            if currentnode.next is None: 
                currentnode.next = node
                break
            currentnode = currentnode.next

    def reverselist(self):
        prev = None
        curr = self.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def printlist(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.val, end = '->')
            currentnode = currentnode.next
        print('None')
        

if '__name__ == __main__':
    head = [0,1,2,3]

    ll = LinkedList()
    for i in head:
        node = ListNode(i)
        ll.insert(node)
    ll.printlist()

    ll.reverselist()
    ll.printlist()
