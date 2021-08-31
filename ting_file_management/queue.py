from ting_file_management.node import Node


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.head_value = None
        self.__length = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        previous_to_be_removed = self.head_value

        if self.__length > 1:
            while previous_to_be_removed.next.next:
                previous_to_be_removed = previous_to_be_removed.next

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = None
        self.__length -= 1

        if value_to_be_removed is None:
            return
        return value_to_be_removed.value

    def search(self, index):
        """Aqui irá sua implementação"""
        value_returned = None
        value_to_be_returned = self.head_value
        index_reverse = self.__length - index - 1
        if index > (self.__length - 1) or index < 0:
            raise IndexError
        if value_to_be_returned:
            while index_reverse > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                index_reverse -= 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
        return value_returned.value
