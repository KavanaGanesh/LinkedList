# Algorithm:
# Create a dummy node : the return is expecting a linkedlist
# current ptr pointing to the dummy
# Given 2 LL which are non-empty : either one of them in non empty - corner case: 3342+546 (here is thouand place is empty - this is corner case)
# iterate through to keep adding until one of the list is None (to explain above statement)
    # fetch l1.val and l2.val else make l1.val and l2.val = 0
    # now add:  res: l1.val + l2.val + carry(this is 0 initially)
    # update th carry:  carry = res // 10 (bcos carry lies in 10's place)
    # update th res(in unit place):  res = res % 10 (bcos res lies in unit's place)

    # update the current link and and current ptr
    # update the l1 link and l1 ptr else in both conditions make it 0
# return the dummy.next

# TO REMEMBER
# l1 = [1,2,3]---- ;it is represented as 3->2->1
# l1 = [4,5,6]---- ;it is represented as 6->5->4



from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, head = None):
        self.head = head 

    def insert(self, node):
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2 or carry:
            if l1 is not None:
                v1 = l1.val
            else:
                v1 = 0

            if l2 is not None:
                v2 = l2.val
            else:
                v2 = 0

            # addition logic basic
            res = v1 + v2 + carry
            
            # considering v1 = 8 ;v2 = 8; res = 8+8 = 16;here carry is 1;want carry then divide by 10
            carry = res // 10

            # want the unit place ; v1 = 8 ;v2 = 8; res = 8+8 = 16; 16 mod 10 =. remainder or unit place is 6
            res = res % 10
            current.next = ListNode(res) # update the link with a node value

            # update the current ptrs
            current = current.next 
            if l1 is not None:
                l1 = l1.next
            else:
                None

            if l2 is not None:
                l2 = l2.next
            else:
                None

        return dummy.next
    

if '__name__ == __main__':
    list1 = [1,2,3] #Output: [5,7,9]
    list2 = [4,5,6]
    ll1 = LinkedList()
    ll2 = LinkedList()

    for i in list1:
        node = ListNode(i)
        ll1.insert(node)
    ll1.printList()

    for i in list2:
        node = ListNode(i)
        ll2.insert(node)
    ll2.printList()

    result = Solution().addTwoNumbers(ll1.head,ll2.head)

    while result:
        print(result.val, end = '->')
        result = result.next
    print('None')