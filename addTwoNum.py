class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num01 = self.getNum(l1=l1)
        num02 = self.getNum(l1=l2)
        ret = num01 + num02
        head = ListNode(ret % 10)
        preNode = head
        ret = ret // 10
        while ret > 0:
            newNode = ListNode(ret % 10)
            preNode.next = newNode
            preNode = newNode
            ret = ret // 10
        return head

    def getNum(self, l1: ListNode):
        num = 0
        i = 1
        while l1.next:
            num += l1.val * i
            i *= 10
            l1 = l1.next
        num += l1.val
        return num






