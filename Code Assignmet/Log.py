# Class that stores the log for proper output info a file

class Log:
    runningP: str
    top3CPU: str
    top3Mem: str
    capH: str
    capM: str

    def __init__(self):
        self.runningP = ""
        self.top3CPU = ""
        self.top3Mem = ""
        self.capH = ""
        self.capM = ""
        return
