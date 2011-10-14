
class Clipt:
    def __init__(self, writer):
        self._writer = writer

    def write(self, key, value):
        self._writer.write(key, value)

    def read(self, key):
        return self._writer.read(key)

    def list(self):
        return self._writer.list()
