class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)  # 1

    def enqueue(self, value):
        if value not in self.data:
            return self.data.append(value)  # 1.1

    def dequeue(self):
        if self.data:
            return self.data.pop(0)  # 1.2
        return None

    def search(self, index):  # 1.3
        print('SELF', self)
        print('INDEX', index)
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError  # 1.4

# python3 -m pytest tests/test_queue.py
# python3 -m venv .venv && source .venv/bin/activate

# referencias
# Tive ajuda de José Carlos - Zeca T06-07
# http://pythontutor.com/live.html#mode=edit
# https://www.geeksforgeeks.org/queue-in-python/
# https://geekflare.com/python-queue-implementation/
# https://geekflare.com/python-stack-implementation/
