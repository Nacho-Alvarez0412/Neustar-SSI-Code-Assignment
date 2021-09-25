# IMPORTS
from typing import List
from ConnectionManager import *
from SSHConnection import *


class Menu:
    conexMgr: ConnectionManager
    sshConnections: List[SSHConnection]
    logger: str

    def __init__(self):
        self.conexMgr = ConnectionManager()
        self.sshConnections = []
        self.logger = ""

    def displayHeader(self):

        print("\n")
        print("\n")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃          LINUX SERVER LOGGER          ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("\n")
        print("\n")

        return

    def inputLoop(self):
        print("Input server IPs separated by comma: ")
        ips = input().split(",")
        validatedIPs = list(map(self.conexMgr.validIP, ips))

        while (None in validatedIPs):

            validatedIPs.remove(None)

            print("\nRetype the invalid ip addresses (or enter '.' to skip): ")
            ips = input().split(",")

            if "." in ips:
                break
            else:
                validatedIPs += ((map(self.conexMgr.validIP, ips)))

        return list(dict.fromkeys(validatedIPs))  # REMOVES DUPLICATES

    def displayIPs(self):
        for connection in self.sshConnections:
            print(connection.ipAddress)
        return

    def mainMenu(self):

        self.displayHeader()
        ips = self.inputLoop()

        if (len(ips) > 0):
            for ip in ips:
                self.sshConnections.append(SSHConnection(ip, "", "", ""))
            print("\nThe following IPs were loaded: ")
            self.displayIPs()

        else:
            print("No IP addresses were loaded")

        return


MENU = Menu()
MENU.mainMenu()
