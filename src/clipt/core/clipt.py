from clipt.writer import writer

class Clipt:
    def __init__(self, the_writer):
        self._writer = the_writer

 
    def write(self, key, value):
        self._writer.write(key, value)

    def read(self, key):
        return self._writer.read(key)
