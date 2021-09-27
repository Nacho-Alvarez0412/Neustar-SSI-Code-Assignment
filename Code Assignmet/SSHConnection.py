import ipaddress
from Log import *


class SSHConnection:
    ipAddress: ipaddress.IPv4Address
    user: str
    pKey: str
    log: Log

    def __init__(self, ipAddress, user, pKey, log):
        self.ipAddress = ipAddress
        self.user = user
        self.pKey = pKey
        self.log = log
