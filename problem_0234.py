
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr)-1

        while left<=right:
            if arr[left]!=arr[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True




        