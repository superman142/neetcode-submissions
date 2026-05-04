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
        self.remove(node)
        self.insert(node)

        return node.value
    

    def insert(self, node: Node):
        node.prev = self.end.prev
        node.next = self.end
        node.prev.next = node
        self.end.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            self.remove(node)
            node.value = value
        else:
            node = Node(key, value)
            self.store[key] = node

        self.insert(node)

        if len(self.store) > self.capacity:
            del self.store[self.start.next.key]
            self.remove(self.start.next)
        
        