# IMPORTS
import ipaddress
from paramiko import SSHClient, AutoAddPolicy
from SSHConnection import *


class ConnectionManager:
    client: SSHClient

    def validIP(self, address):
        try:
            ip = ipaddress.ip_address(address)
            print("\nIP address {} is valid. Stored successfully".format(address))
            return ip
        except ValueError:
            print("\nIP address {} is not valid".format(address))
            return None

    def connect(self, sshConnection: SSHConnection):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(sshConnection.ipAddress.exploded,
                            username="ubuntu", key_filename=sshConnection.pKey)

        stdin, stdout, stderr = self.client.exec_command("hostname")

        if stdout.channel.recv_exit_status() == 0:
            print(f'STDOUT: {stdout.read().decode("utf8")}')

        else:
            print(f'STDERR: {stderr.read().decode("utf8")}')

        stdin.close()
        stdout.close()
        stderr.close()
        self.client.close()

        return
