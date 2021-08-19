from ting_file_management.node import Node


class Queue:
    def __init__(self):
        self._head_value = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self._head_value})"

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        head_element = Node(value=value)
        head_element._next = self._head_value
        self._head_value = head_element
        self.__length += 1

    def dequeue(self):
        value_element = self._head_value
        if self.__length > 1:
            while value_element._next._next:
                value_element = value_element._next

            value_to_be_removed = value_element._next
            value_element._next = None
            self.__length -= 1
            return value_to_be_removed._value
        value_element._value = None
        self.__length -= 1
        return value_element._value

    def search(self, index):
        value_returned = None
        value_to_be_returned = self._head_value
        if index not in range(self.__length):
            raise IndexError

        if value_to_be_returned:
            while index < self.__length - 1 and value_to_be_returned._next:
                value_to_be_returned = value_to_be_returned._next
                index += 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned._value)
        return value_returned._value


if __name__ == "__main__":
    # TESTE 1
    # assert len(queue) == 1
    # queue = Queue()
    # queue.enqueue(42)
    # print(len(queue))

    # TESTE 2
    # assert len(queue) == 2
    # assert given == 42
    # queue = Queue()
    # queue.enqueue(42)
    # queue.enqueue(43)
    # queue.enqueue(44)
    # given = queue.dequeue()
    # print(queue)
    # print(given)

    # TESTE 3
    # assert queue.search(0) == 42
    # assert queue.search(1) == 43
    # assert queue.search(2) == 44
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(43)
    queue.enqueue(44)
    print(queue.search(1))
