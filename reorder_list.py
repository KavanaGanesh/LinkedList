# Algorithm: [1,2,3,4,5]
# 1. Find the middle element of the LL (achieved using 2 pointers - slow and fast)
    # slow and fast both pointing to head
    # while fast and fast.next is not null
        # increment slow by 1 position
        # increment fast by 2 positions
    # the slow pointer is the middle element
# 2.Reverse the second part of the list - that is from middle element
    # reversing basic 3 pointers with prev, current and nxt
    # to remember : before reversing the last element .next should point to None
# 3.To merge the first = [1,2,3] and reversed list , second = [5,4]
    # after reversed in step2, the 'prev' pointer points to beginning of the list so 'second = prev'
    # trick : store the first.next amd second.next links to temp variables
    # while second is not None:
        # tmp1 = first.next
        # tmp2 = second.next
        # point first.next = second
        # point second.next = tmp1
        # make first = tmp1
        # make second = tmp2
from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def insert(self, val):
        if self.head is None:
            self.head = node
            return 
        
        already_existed = self.head
        while True:
            if already_existed.next is None:
                already_existed.next = node
                break
            already_existed = already_existed.next

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end = '->')
            current_node = current_node.next
        print('None')


class Solution:
    # find the middle of the LL first
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list
        prev = None
        current = slow.next
        slow.next = None
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # merge first half of the list with the reversed list
        # first = [1->2->3]
        # second = [5->4]
        # output = [1->5->2->4->3]
        first = head 
        second = prev
        while second is not None:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second #[1->5]
            second.next = tmp1
            first = tmp1
            second = tmp2

if '__name__ == __main__':
    # head = [2,4,6,8] #Output: [2,8,4,6]
    head = [2,4,6,8,10] #Output: [2,10,4,8,6]
    ll = LinkedList()
    for i in head:
        node = ListNode(i)
        ll.insert(node)
    ll.printList()
    Solution().reorderList(ll.head)
    ll.printList()




