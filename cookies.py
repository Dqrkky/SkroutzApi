import os
import pickle

class Cookie:
    def __init__(self, filename :str=None):
        self.filename = filename
        self.exists = self.filename in os.listdir()
    def __enter__(self):
        return self
    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass
    def read(self):
        with open(
            file=self.filename,
            mode="rb+"
        ) as fp:
            return pickle.load(
                file=fp
            )
    def write(self, cookies :any=None):
        with open(
            file=self.filename,
            mode="wb+"
        ) as fp:
            return pickle.dump(
                obj=cookies,
                file=fp
            )