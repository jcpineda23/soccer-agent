class Memory:
    def __init__(self):
        self.history = []

    def save(self, step, result):
        self.history.append({"step": step, "result": result})

    def recall(self):
        return self.history