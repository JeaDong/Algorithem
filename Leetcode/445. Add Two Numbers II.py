class Solution:
    def addTwoNumbers(self, l1, l2):
        s1,s2 = [],[]
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        s = 0
        dummy = ListNode(0)
        while s1 or s2 or s:
            if s1:
                s += s1.pop().val
            if s2:
                s += s2.pop().val
            cur = ListNode(s % 10)#actually I use - 10 before
            cur.next = dummy.next
            dummy.next = cur
            s //= 10
        return dummy.next
		#why add s in last loop?
		#when [5],[5],if s not in loop,the solution will return [0] not [1,0]
class Solution:
    def addTwoNumbers(self, l1, l2):
        s = self.convert(l1) + self.convert(l2)
        return self.MergeList(s)
    
    def convert(self,li):
        s = ''
        while li:
            s += str(li.val)
            li = li.next
        return int(s)
    
    def MergeList(self,s):
        arr = list(str(s))
        head = cur = ListNode(0)
        for i in arr:
            cur.next = ListNode(int(i))
            cur = cur.next
        return head.next
		