from typing import *
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        return q == q[::-1]

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # 런너
        while fast and fast.next:
            fast = fast.next.next
            # 역순 연결리스트 rev 생성
            rev, rev.next, slow = slow, rev, slow.next
        # palindrome이 홀수인 경우, 짝수인 경우 다르게 처리
        # 홀수인 경우 가운데가 남기 때문에 slow런너를 한 칸 더 보내준다
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev