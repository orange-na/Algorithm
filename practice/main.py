class Node():
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList():
    def __init__(self, head = None):
        self.head = head
    

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        

if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    print(l.head.next.prev.data)
