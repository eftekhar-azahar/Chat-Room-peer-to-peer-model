# Server is only being used to find connections
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        # the server keeps track of the newly joining peers in the network
        datagram = datagram.decode('utf-8')
        if datagram == "Connect":
            addresses = "\n".join([str(x) for x in self.clients])
            self.transport.write(addresses.encode('utf-8'), addr)
            self.clients.add(addr)


if __name__ == '__main__':
    print("Server is running ............... ")
    reactor.listenUDP(9999, Server())
    reactor.run()
