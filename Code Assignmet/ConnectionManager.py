# IMPORTS
import ipaddress


class ConnectionManager:

    def validIP(self, address):
        try:
            ip = ipaddress.ip_address(address)
            print("\nIP address {} is valid. Stored successfully".format(address))
            return ip
        except ValueError:
            print("\nIP address {} is not valid".format(address))
            return None
