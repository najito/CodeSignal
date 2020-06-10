# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    str_a = ''
    str_b = ''
    curr_a = a
    curr_b = b
    while curr_a:
        str_a += ((4 - len(str(curr_a.value))) * '0') + str(curr_a.value)
        curr_a = curr_a.next
    while curr_b:
        str_b += ((4 - len(str(curr_b.value))) * '0') + str(curr_b.value)
        curr_b = curr_b.next
    total = int(str_a) + int(str_b)
    node = ListNode(None)
    if total == 0:
        return [0]
    while total != 0:
        node.value = total % 10000
        new_node = ListNode(None)
        new_node.next = node
        node = new_node
        total //= 10000
    return node.next
    
    
    