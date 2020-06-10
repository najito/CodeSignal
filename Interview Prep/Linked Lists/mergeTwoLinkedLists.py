# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    curr1 = l1
    curr2 = l2
    try:
        result = l1 if l1.value < l2.value else l2
    except AttributeError:
        if l1 == None:
            result = l2
        else:
            result = l1
    while curr1 and curr2:
        if curr1.value < curr2.value:
            while curr1 and curr1.value < curr2.value:
                follow = curr1
                curr1 = curr1.next
            follow.next = curr2
        else:
            while curr2 and curr2.value <= curr1.value:
                follow = curr2
                curr2 = curr2.next
            follow.next = curr1
    return result
        