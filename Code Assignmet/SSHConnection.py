import ipaddress


class SSHConnection:
    ipAddress: ipaddress.IPv4Address
    user: str
    pKey: str
    log: str

    def __init__(self, ipAddress, user, pKey, log):
        self.ipAddress = ipAddress
        self.user = user
        self.pKey = pKey
        self.log = log
