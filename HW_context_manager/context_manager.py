import logging

logging.basicConfig(level=logging.ERROR)

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is IndexError:
            logging.error(f"IndexError: {exc_val}")
            return True
        return False


try:
    with FileManager('example.txt') as f:
        data = [1, 2, 3]
        print(data[5])
except Exception as e:
    print(f"an exception has occurred: {e}")
