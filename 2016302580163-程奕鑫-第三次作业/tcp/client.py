from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

serverAddress = ("1.1.2.1", 8080)
tcpClientSocket.connect(serverAddress)

while True:
    sendData = input("Please write here:")
    if len(sendData) > 0:
        tcpClientSocket.send(sendData.encode('utf8'))
    else:
        print("Nothing has been sent")
        break

    recv = tcpClientSocket.recv(1024)
    print("1.1.2.1:\n" + recv.decode('utf8'))

socket.close()