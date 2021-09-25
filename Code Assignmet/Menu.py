# IMPORTS
from ConnectionManager import *


class Menu:
    conexMgr = ConnectionManager()
    sshConnections = []
    logger = None

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

            print("Retype the invalid ip addresses (or enter '.' to skip): ")
            ips = input().split(",")

            if "." in ips:
                break
            else:
                validatedIPs += ((map(self.conexMgr.validIP, ips)))

        return list(dict.fromkeys(validatedIPs))  # REMOVES DUPLICATES

    def displayIPs(self, ips):
        for ip in ips:
            print(ip)
        return

    def mainMenu(self):

        self.displayHeader()
        ips = self.inputLoop()
        print("The following IPs were loaded: ")
        self.displayIPs(ips)

        return


MENU = Menu()
MENU.mainMenu()
