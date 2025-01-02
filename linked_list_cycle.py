# Definition for singly-linked list.
# Algorithm:
# 1. Keep 2 pointers :  slow and a fast pointer
# 2. Iterate through checking with the condition while fast and fast.next exists
    # 3. move slow pointer by one step
    # 4. move fast pointer by 2 step
    # 5. once they become equal : loop is detected
# return boolean value based on that


from typing import Optional

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        if self.head is None:
            self.head = node
            return 
        
        already_existed = self.head
        while True:
            if already_existed.next is None:
                already_existed.next = node
                break
            already_existed = already_existed.next

            
    # TODO:
    def connect_loop(self, index):
        if index > 0:
            pass

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end = '->')
            current_node = current_node.next
        print('None')

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s_pointer = head
        f_pointer = head

        while f_pointer and f_pointer.next:
            s_pointer = s_pointer.next
            f_pointer = f_pointer.next.next
            if s_pointer == f_pointer:
                return True
        return False
    

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next = head.next 
# '''here it returns True if if above line is uncommented'''


# print(Solution().hasCycle(head))
if '__name__ == __main__':
    head = [1,2,3,4] #Output: true
    index = 1 
    ll = LinkedList()
    for i in head:
        node = ListNode(i)
        ll.insert(node)
    ll.printList()

    result = Solution().hasCycle(ll.head)
    print(result)







        