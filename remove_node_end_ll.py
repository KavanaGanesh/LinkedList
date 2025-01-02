# Algorithm:
# 1. Create a class listnode - that hold the class attributes
    # Using constructor to store val and next
# 2. CReate a class Linkedlist for the basic operation that involves insertion , printing (deletion as needed)
    # Using constructor to store the head
    # implement the insert method for each node being created - the insert method should consider
        # if LL is empty? - make the node1 as the head
        # if LL has only one already existed node? -  make already existed node as the head of LL. Make sure to point the already existed node's next to the node i created
        # if LL has few already existed nodes? - connect already existed node.next to already existed node
    # implement the print method to print the entire LL after insertion:
        # create a pointer to point to the head of the node
        # check for condition - if the next node exists?
            # if yes, print the vale, connect the next to the upcoming node
# 3. Create a class to remove the Nth node from end
    # create a dummy node with(val=0, next = head)
    # Keep 2 pointers - left pointing to dummy, right pointing to the head of the LL (Ex:dummy->1->2->3->4->5)
    # iterate through while - making right pointer to maintain exactly 2 position from left pointer
    # iterate through while - move the right and left both pointers by 1 step until right is not None
    # The above actions gives: left pointer at = 3, right pointer = None(that is after 5)
    # now connect left.next to left.next.next
    # the question asks to return the list, so return dummy.next




from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head 
    
    def insert(self, node):
        if self.head is None:
            self.head = node
            return
    
        alread_existed = self.head
        while True:
            if alread_existed.next is None:
                alread_existed.next = node
                break
            alread_existed = alread_existed.next

    def print_ll(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end = '->')
            current_node = current_node.next
        print('None')


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n>0:
            right = right.next
            n = n-1

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    


# How to create a object from these 3 classes and do the executions?
# create an object ll form LinkedList - creating an empty LL
# Iterate through the values given
# for each value create an node object using class Listnode
    # use insert method insert the node object to the Linkedlist object
# finally using print method print the entire Linkedlist

# Similarly create a result object to remove nth node from class solution
# pass the linkedlist object as the head of the node
# print the entire result with val and next connection

if '__name__ == __main__':
    head = [1,2,3,4] #Output: [1,2,4]
    n = 2
    # head = [1,2] #Output: [2]
    # n = 2

    ll = LinkedList()
    for i in head:
        node = ListNode(i)
        ll.insert(node)
    ll.print_ll()

    result = Solution().removeNthFromEnd(ll.head, 2)


    while result:
        print(result.val, end = '->')
        result = result.next
    print('None')

