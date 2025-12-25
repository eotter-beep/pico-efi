import os
class Process():
    def cpu_count(disableprint):
        if not disableprint:
            print(os.cpu_count())
        if disableprint:
            return os.cpu_count()
    def list(disableprint):
        if not disableprint:
            print(os.listdir())
        if disableprint:
            return os.listdir()
