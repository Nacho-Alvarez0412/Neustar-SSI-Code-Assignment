import ipaddress
from Log import *


class SSHConnection:
    ipAddress: ipaddress.IPv4Address
    host: str
    user: str
    pKey: str
    log: Log

    def __init__(self, ipAddress, user, pKey, host):
        self.ipAddress = ipAddress
        self.user = user
        self.pKey = pKey
        self.host = host
        self.log = Log()

    def getLog(self):
        log = f"Server Ip: {self.ipAddress}\n\nINIT OF LOG\n\n"
        log += f"CURRENT RUNNING PROCESSES\n\n {self.log.runningP}\n\n"
        log += f"TOP 3 APPLICATIONS WITH MORE CPU USAGE \n\n {self.log.top3CPU}\n\n"
        log += f"TOP 3 APPLICATIONS WITH MORE MEMORY USAGE \n\n {self.log.top3Mem}\n\n"
        log += f"LEFT CAPACITY HUMAN READABLE \n\n {self.log.capH}\n\n"
        log += f"LEFT CAPACITY MACHINE READABLE \n\n {self.log.capM}\n\n"
        return log

    def logOutput(self):
        # str(self.host)[:-1] removes "\n" from hostname
        file = open(str(self.host)[:-1]+".txt", "a")
        file.write(self.getLog())
        file.close()
