class Node:

    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]

        self.addNodeToEnd(node)

        return node.value
    

    def addNodeToEnd(self, node: Node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = self.end.prev
        node.next = self.end
        node.prev.next = node
        self.end.prev = node

    def removeNodeFromStart(self):
        node = self.start.next
        
        self.start.next.next.prev = self.start
        self.start.next = self.start.next.next
        

        return node.key


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
        else:
            node = Node(key, value)
            self.store[key] = node
        
        self.addNodeToEnd(node)

        if len(self.store.keys()) > self.capacity:
            del self.store[self.removeNodeFromStart()]
        
        

        
