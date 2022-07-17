class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next

    def __str__(self) -> str:
        return f"node data:{self.data} --> {self.next}"


def print_ll(head):
    while head:
        print(head.data)
        head = head.next

def count_nodes(head):
    count = 0
    while head:
        count+=1
        head = head.next
    print(f"There are {count} nodes in the list")

def insert_at_last(head, data):
    if not head:
        return Node(data)
    ptr = head    
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head


def insert_at_beg(head, data):
    p = Node(data)
    p.next = head
    head = p
    return head

def remove_from(head, key):
    current = head
    previous = None
    found = False

    while current and not found:
        if current.data == key and current is head:
            found = True
            head = current.next
        elif current.data == key:
            found = True
            previous.next = current.next
        else:
            previous = current
            current = current.next
    return head



a = Node(2, Node(4, Node(8, Node(16)))) 
a = remove_from(a, 16)
print_ll(a)
count_nodes(a)
