# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        # p, q = headA, headB
        # s = []
        # while p:
        #     s.append(p)
        #     p = p.next
        # while q:
        #     if q in s:
        #         return q
        #     q = q.next
        # return None

        lengthA, lengthB = 0, 0
        p, q = headA, headB
        while p:
            p = p.next
            lengthA += 1
        while q:
            q = q.next
            lengthB += 1

        p, q = headA, headB
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                p = p.next
        else:
            for i in range(lengthB - lengthA):
                q = q.next
        while p and q:
            if p == q:
                return p
            q = q.next
            p = p.next
        return None

if __name__ == '__main__':
    res = Solution().getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5])
    print(res)
