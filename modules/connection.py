# ASWP v0.0.1pa1

import socket
from json import dumps
import os

class Connection():
    def __init__(self, ip):
        config = dumps(os.getcwd() + 'config.json')['connection']
        self.conn = self.setup(ip, config['port'])
        pass

    def setup(self, ip, port):
        self.conn = socket.socket()
        self.conn.bind(ip, port)
