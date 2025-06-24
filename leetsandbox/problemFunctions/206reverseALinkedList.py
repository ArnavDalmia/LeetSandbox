
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListFunctionality(head):
    prev = None
    current = head

    if head == None or head.next == None:
        return head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main(values):
    print(f"Original list: {values}")
    
    # Create linked list
    head = create_linked_list(values)
    print(f"Created linked list: {print_list(head)}")
    
    # Reverse the list
    reversed_head = reverseListFunctionality(head)
    reversed_values = print_list(reversed_head)
    print(f"Reversed linked list: {reversed_values}")

# EXAMPLE
# main([1, 2, 3, 4, 5])
# main([1, 2])
# main([1])
