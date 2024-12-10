# Created on iPad (Timur).
# from fractions import Fraction as f
import socket

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        data, addr = sock.recvfrom(1024)
        print("received message: %s" % data)
if __name__ == "__main__":
    main()