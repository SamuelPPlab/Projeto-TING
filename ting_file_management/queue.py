from collections import deque


class Queue:
    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def is_empty(self):
        return not len(self._deque)

    def __str__(self):
        return "Deque(" + ", ".join(str(x) for x in self._deque) + ")"

    def __iter__(self):
        for noh in self._deque:
            yield noh.value

    def enqueue(self, value):
        self._deque.append(value)

    def dequeue(self):
        try:
            return self._deque.popleft()
        except Exception as e:
            print(e.args)

    def search(self, index_search):
        for index, noh in enumerate(self._deque):
            if index == index_search:
                return noh
        raise IndexError(f'Index {index_search} not found')


if __name__ == '__main__':
    teste = Queue()
    teste.enqueue(1)
    print(teste.is_empty())  # False
    teste.dequeue()
    print(teste.is_empty())  # True
    teste.enqueue(10)
    teste.enqueue(120)
    print(teste)  # Deque(10,120)
    print(teste.search(0))  # 10
    print(teste.search(1))  # 120
    teste.dequeue()
    teste.dequeue()
    print(teste)  # Deque(10,120)
    teste.enqueue(13)
    print(teste)  # Deque(13)
    print(teste.search(0))  # 13
    print(teste.search(1))  # IndexError Index 1 not found
    teste.dequeue()
    print(teste.search(1))  # IndexError Index 1 not found
