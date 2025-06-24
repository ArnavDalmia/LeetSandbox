
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linkedListCycleFunctionality(head):
    if head == None or head.next == None:
        return False
    
    # Floyd's cycle detection algorithm (tortoise and hare)
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Pointers meet, cycle detected
            return True
    
    return False

def create_linked_list_with_cycle(values, cycle_pos):
    """Create a linked list with a cycle at cycle_pos (-1 means no cycle)"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # Create cycle if cycle_pos is valid
    if 0 <= cycle_pos < len(nodes):
        current.next = nodes[cycle_pos]
    
    return head

def print_list_with_cycle_info(head, max_nodes=20):
    """Print list values, detecting cycles"""
    if not head:
        return "Empty list"
    
    visited = set()
    current = head
    values = []
    
    while current and len(values) < max_nodes:
        if id(current) in visited:
            values.append(f"{current.val}(cycle detected)")
            break
        visited.add(id(current))
        values.append(str(current.val))
        current = current.next
    
    return " -> ".join(values)

def main(values, cycle_pos=-1):
    head = create_linked_list_with_cycle(values, cycle_pos)
    result = linkedListCycleFunctionality(head)
    
    print(f"List values: {values}")
    if cycle_pos >= 0:
        print(f"Cycle at position: {cycle_pos}")
    else:
        print("No cycle")
    
    print(f"List structure: {print_list_with_cycle_info(head)}")
    print(f"Has cycle: {result}")

# EXAMPLE
# main([3, 2, 0, -4], 1)  # Cycle back to position 1
# main([1, 2], 0)         # Cycle back to position 0  
# main([1], -1)           # No cycle
