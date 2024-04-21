# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()  # 结果链表
        current = result
        # 进位
        carry = 0
        # 当前位
        total = 0
        while l1 or l2 or total:
            x = l1.val
            y = l2.val
            total = (x + y + carry) % 10
            carry = total // 10

            current.next = ListNode(total)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return current


if __name__ == '__main__':
    res = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])
    print(res)