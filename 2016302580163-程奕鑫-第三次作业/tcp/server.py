from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

address = ('', 8080)
tcpSerSocket.bind(address)

tcpSerSocket.listen(5)

while True:
    newSocket, clientSocket = tcpSerSocket.accept()
    while True:
        receiveData = newSocket.recv(1024)

        if len(receiveData) > 0:
            print("1.1.1.1:\n" + receiveData.decode('utf8'))
        else:
            break

        sendData = input("1.1.2.1:\n")
        newSocket.send(sendData.encode('utf8'))
    newSocket.close()