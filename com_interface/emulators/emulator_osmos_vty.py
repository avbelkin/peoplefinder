# -*- coding: utf-8 -*-
import SocketServer
import socket
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        print("Cient {0} connected.".format(self.client_address[0]))

    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            time.sleep(1)

    def finish(self):
        print "Cient {0} dis connected".format(self.client_address[0])


if __name__ == "__main__":

    HOST, PORT = "localhost", 4242
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
