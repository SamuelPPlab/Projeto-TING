    def __str__(self):
        return "Deque(" + ", ".join(map(lambda x: str(x), self.fila)) + ")"