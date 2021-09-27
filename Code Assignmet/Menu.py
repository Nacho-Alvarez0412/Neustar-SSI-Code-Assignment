# IMPORTS
from typing import List
from ConnectionManager import *
from SSHConnection import *

# Class that displays menu


class Menu:
    conexMgr: ConnectionManager
    sshConnections: List[SSHConnection]
    logger: str

    def __init__(self):
        self.conexMgr = ConnectionManager()
        self.sshConnections = []
        self.logger = ""

    # Input: None
    # Description: Displays the header in commandline
    # Output: None
    def displayHeader(self):

        print("\n")
        print("\n")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃          LINUX SERVER LOGGER          ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("\n")
        print("\n")

        return

    # Input: None
    # Description: Receives the IPs separated by commas, in case one ip is invalid, stores the rest and ask for the invalid again
    # Output: The list of IPS verified and free of duplicates
    def inputLoopIPs(self):
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

    # Input: None
    # Description: Display the loaded IPs for user validation
    # Output: None
    def displayIPs(self):
        for connection in self.sshConnections:
            print(connection.ipAddress)
        return

    # Input: None
    # Description: Receives the full path of each of the SSH keys needed for the connection
    # Output: None

    # Important note: For AWS VM the .pem key can be used, for other virtual machines
    # a OpenSSH private key format is needed in orther for paramiko to work.
    def inputLoopKeys(self):
        oneForAll = False
        keyPath = ""
        for connection in self.sshConnections:
            if(not oneForAll):
                print("\nInput key path for stablishing SSH Connection: ")
                keyPath = input()

                print("\nDo you want to use this key for all current connections? Y/N")
                decision = input().capitalize()

                if decision == "Y" or decision == "YES":
                    oneForAll = True

            connection.pKey = keyPath

        return

    # Input: None
    # Description: Receives the user of each of the VMs that is desired to stablish a connection
    # Output: None
    def inputLoopUser(self):
        oneForAll = False
        user = ""
        for connection in self.sshConnections:
            if(not oneForAll):
                print("\nInput user for stablishing SSH Connection: ")
                user = input()

                print("\nDo you want to use this user for all current connections? Y/N")
                decision = input().capitalize()

                if decision == "Y" or decision == "YES":
                    oneForAll = True

            connection.user = user

        return

    # Input: None
    # Description: Displays the main menu, stablishes connection and outputs the logs in .txt files
    # Output: None

    def mainMenu(self):

        self.displayHeader()
        ips = self.inputLoopIPs()

        if (len(ips) > 0):
            for ip in ips:
                self.sshConnections.append(SSHConnection(ip, "", "", ""))
            print("\nThe following IPs were loaded: ")
            self.displayIPs()
            self.inputLoopKeys()
            self.inputLoopUser()
            print("\nExecuting logging script")

            for connection in self.sshConnections:
                self.conexMgr.connect(connection)
                connection.logOutput()

        else:
            print("No IP addresses were loaded")
            return

        print("\n\nAll logs have been realized successfully, they can be found by the hostname of each logged system")
        return


MENU = Menu()
MENU.mainMenu()
