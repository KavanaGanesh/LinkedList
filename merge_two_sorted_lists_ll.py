# Algorithm:
# 3cases to consider: 
# create a dummy node to start: where current ptr is at dummy node
    # if both lists has values - iterate through while
        # if list1.val<=list2.val :
            # connect the pointer to the list1 node
            # move the list1 to list1.next
            # move the current to current.next
        # elif list1.val>list2.val :
            # connect the pointer to the list2 node
            # move the list2 to list2.next
            # move the current to current.next

    # if list1 is empty
            # connect the pointer to the list2 node
            # move the list2 to list2.next
            # move the current to current.next

    # if list2 is empty
            # connect the pointer to the list1 node
            # move the list1 to list1.next
            # move the current to current.next






from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, val):
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next
        
    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end = '->')
            current_node = current_node.next
        print('None')

class Solution():
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, None)
        current = dummy_node
        # current is a anchor pointer keep track of the elements for comparision with each two listnode

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                current.next = list2
                list2 = list2.next
            current = current.next


        if list1:
            current.next = list1
            list1 = list1.next
        if list2:
            current.next = list2
            list2= list2.next


        return dummy_node.next


# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)



# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)

if '__name__==__main__':
    list1 = [1,2,4]
    list2 = [1,3,5]
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

    result = Solution().mergeTwoLists(ll1.head,ll2.head)

    while result:
        print(result.val, end = '->')
        result = result.next
    print('None')