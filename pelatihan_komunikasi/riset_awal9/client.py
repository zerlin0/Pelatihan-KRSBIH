import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addRobot1 = ("localhost", 9979)
addRobot2 = ("localhost", 9979)
addRobot3 = ("localhost", 9979)

def kirimPesan(message, sender):
    pesan = message.encode('utf-8')
    IPsender = sender
    client.sendto(pesan,IPsender)

if __name__ == '__main__':
    while True:
        kirimPesan("hello", addRobot1)
        kirimPesan("berhenti", addRobot1)
        break