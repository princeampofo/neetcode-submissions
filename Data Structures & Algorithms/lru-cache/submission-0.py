class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev_node = self.right.prev

        node.prev = prev_node
        prev_node.next = node

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        node.prev , node.next = None, None

        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

