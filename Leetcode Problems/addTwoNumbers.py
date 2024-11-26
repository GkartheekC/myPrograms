# Adds two numbers represrnted by linked lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        def outputMaker(l1, l2, carry):

            if l1.next != None and l2.next != None:
                if l1.val + l2.val < 10:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val, outputMaker(l1.next, l2.next, 0)))
                    else:
                        if l1.val + l2.val < 9:
                            return (ListNode(l1.val + l2.val + 1, outputMaker(l1.next, l2.next, 0)))
                        else:
                            return (ListNode(0, outputMaker(l1.next, l2.next, 1)))
                else:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val - 10, outputMaker(l1.next, l2.next, 1)))
                    else:
                        return (ListNode(l1.val + l2.val - 9, outputMaker(l1.next, l2.next, 1)))
            
            elif l1.next != None and l2.next == None:
                if l1.val + l2.val < 10:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val, singleList(l1.next, 0)))
                    else:
                        if l1.val + l2.val < 9:
                            return (ListNode(l1.val + l2.val + 1, singleList(l1.next, 0)))
                        else:
                            return (ListNode(0, singleList(l1.next, 1)))
                else:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val - 10, singleList(l1.next, 1)))
                    else:
                        return (ListNode(l1.val + l2.val - 9, singleList(l1.next, 1)))

            elif l1.next == None and l2.next != None:
                if l1.val + l2.val < 10:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val, singleList(l2.next, 0)))
                    else:
                        if l1.val + l2.val < 9:
                            return (ListNode(l1.val + l2.val + 1, singleList(l2.next, 0)))
                        else:
                            return (ListNode(0, singleList(l2.next, 1)))
                else:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val - 10, singleList(l2.next, 1)))
                    else:
                        return (ListNode(l1.val + l2.val - 9, singleList(l2.next, 1)))

            
            else:
                if l1.val + l2.val < 10:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val, None))
                    else:
                        if l1.val + l2.val < 9:
                            return (ListNode(l1.val + l2.val + 1, None))
                        else:
                            return (ListNode(0, (ListNode(1, None))))
                else:
                    if carry == 0:
                        return (ListNode(l1.val + l2.val - 10, ListNode(1, None)))
                    else:
                        return (ListNode(l1.val + l2.val - 9, ListNode(1, None)))
        

        def singleList (l1, carry):

            if l1.next != None:
                if carry == 0:
                    return (ListNode(l1.val, singleList(l1.next, 0)))
                else:
                    if l1.val != 9:
                        return (ListNode(l1.val + 1, singleList(l1.next, 0)))
                    else:
                        return (ListNode(0, singleList(l1.next, 1)))
            else:
                if carry == 0:
                    return (ListNode(l1.val, None))
                else:
                    if l1.val != 9:
                        return (ListNode(l1.val + 1, None))
                    else:
                        return (ListNode(0, ListNode(1, None)))


        return(outputMaker(l1, l2, 0))