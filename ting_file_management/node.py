class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def __str__(self):
        return f"Node(value={self._value}, next={self._next})"
