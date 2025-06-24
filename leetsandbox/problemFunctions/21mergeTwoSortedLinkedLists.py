
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoListsFunctionality(list1, list2):
    dummy = ListNode()
    node = dummy

    # now we created a dummy
    currentOne = list1
    currentTwo = list2
    while currentOne and currentTwo:
        if currentOne.val < currentTwo.val:
            node.next = currentOne
            currentOne = currentOne.next
        elif currentOne.val >= currentTwo.val:
            node.next = currentTwo
            currentTwo = currentTwo.next
        node = node.next
    node.next = currentOne or currentTwo  # if one has carry over
    return dummy.next

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

def main(list1_values, list2_values):
    output = f"""List 1: {list1_values}
List 2: {list2_values}"""
    
    # Create linked lists
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    
    # Merge the lists
    merged = mergeTwoListsFunctionality(list1, list2)
    merged_values = print_list(merged)
    output += f"\nMerged sorted list: {merged_values}"
    
    return output

# EXAMPLE
# main([1, 2, 4], [1, 3, 4])
# main([], [])
# main([], [0])
