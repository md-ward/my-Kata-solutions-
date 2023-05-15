


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1 = str(head)
        temp2 = str(head)[::-1]
        print(temp1,temp2)
        if temp1 == temp2:
            return True
        else:
            return False
print(Solution.isPalindrome(head=[[121]]))