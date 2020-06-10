# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    fakeHead = ListNode(None)
    fakeHead.next = l
    current = fakeHead
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
    return fakeHead.next