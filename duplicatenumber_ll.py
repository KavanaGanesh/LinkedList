# its a linkedlist cycle detection problem
# algorithm used is Floyd's Tortoise and Hare
# Algorithm:
# 1. Create a class listnode - that hold the class attributes
    # Using constructor to store val and next
# 2. CReate a class Linkedlist for the basic operation that involves insertion , printing (deletion as needed)
    # Using constructor to store the head
    # implement the insert method for each node being created - the insert method should consider
        # if LL is empty? - make the node1 as the head
        # if LL has only one already existed node? -  make already existed node as the head of LL
        # if LL has few already existed nodes? - connect already existed node.next to already existed node
    # implement the print method to print the entire LL after insertion:
        # create a pointer to point to the head of the node
        # check for condition - if the next node exists?
            # if yes, print the vale, connect the next to the upcoming node
# 3.Create a class that to find the duplicate digit
    # first: need to detect the cycle
        # 2 pointer, fast and slow both pointing at head
        # slow moves by 1 step, fast moves by 2 step
        # when both fast and slow meets -cycle/loop is detected
    # second: to find the beginning of the cycle
        # need 2 pointers, slow(and fast both pointing atcycle) and slow2 pointing at beginning of the list
        # move slow and slow2 by 1 step
        # check for condition where they meet -  if they meet at one point (that is the beginning of the cycle)

"""Rememeber 1st element is not a part of the Linkedlist: that means no pointer connected to 1st element"""
# from typing import Optional

# class ListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# class LinkedList():
#     def __init__(self, head = None):
#         self.head = head

#     def insertNode(self, value):
#         if self.head is None:
#             self.head = node
#             return
        
#         already_existed = self.head
#         while True:
#             if already_existed.next is None:
#                 already_existed.next = node
#                 break
#             already_existed = already_existed.next

#     def printList(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value, end = '->')
#             current_node = current_node.next
#         print('None')

# class Solution:
#         def findDuplicate(self, head:Optional[ListNode])->Optional[ListNode]:
#             slow = head
#             fast = head
#             while fast and fast.next is not None:
#                 slow = slow.next
#                 fast = fast.next.next
#                 if slow == fast:
#                     return slow.value
#                     # break
            
            # slow2 = head
            # # the duplicate number is the beginning of the cycle
            # while slow and slow2 is not None:
            #     slow = slow.next
            #     slow2 = slow2.next
            #     if slow == slow2:
            #         return slow


# kav solution:
# requirement is O(1) extra space. That means 2 pointers. But i cannot use binary search on the array list
# instead let me use binary search on the range offered (1,n) but there are n+1 numbers in the range
# 1) find the mid with low = 1, since the expalnantion clarifies that repeated number can be 2 or more 
# when is the repeated number 2 or more means - then it will be [1,2,3,2,2] : here in one more position it can be 4 as well making 2 from repeating thrice to twice
# therefore high = n-1
# 2) for each value in head - check if the value is less than the mid; if yes increase its count 
# 3) if the count is greater than the mid - that shows number is repeated move high to mid
# 4) else move low to mid+1
class Solution:
        def findDuplicate(self, head):
            n = len(nums)
            low = 1
            high = n-1

            while low < high:
                mid = low + (high-low)//2
                count = 0
                for n in head:

                    if n <= mid:
                        count = count+1
                if count > mid:
                    high = mid
                else:
                    low = mid+1
            return low
  

if '__name__ == __main__':
  
    # nums = [1,2,3,2,2] #Output: 2
    nums = [1,2,3,4,4] #Output: 4
    # ll = LinkedList()
    # for i in nums:
    #     node = ListNode(i)
    #     ll.insertNode(node)
    # ll.printList()
    # result = Solution().findDuplicate(ll.head)
    # print(result)
    print(Solution().findDuplicate(nums))


