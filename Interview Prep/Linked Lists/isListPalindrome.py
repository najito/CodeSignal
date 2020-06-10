# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    curr = l
    check = []
    try:
        while curr:
            check.append(curr.value)
            curr = curr.next
    except AttributeError:
        print(curr)
    return check == check[::-1]

