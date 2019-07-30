"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumbers(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        carry = 0
        head = None
        prev = None
        while l1 != None or l2 != None:
            if l1 == None:
                s = l2.val
                l2 = l2.next
            elif l2 == None:
                s = l1.val
                l1 = l1.next
            else:
                s = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            digit = (s + carry) % 10
            node = ListNode(digit)
            carry = (s + carry) // 10
            if head is None:
                head = node
            elif head.next is None:
                head.next = node
            else:
                prev.next = node
            prev = node

        if carry > 0:
            prev.next = ListNode(carry)
            
        return head


# (2 -> 4 -> 3) + (5 -> 6 -> 4) -> 7 -> 0 -> 8