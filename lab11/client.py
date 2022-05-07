import sys
import socket


n = len(sys.argv)
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
host = socket.gethostname()
port = int(sys.argv[1])

s.connect((host, port))

while True:
    print("Enter 1 for sending message to server")
    print("Enter 0 for exit")
    ch = int(input())
    if ch == 1:
        msg = input("Enter the message to be send to server: ")
        s.send(str.encode(msg))
        recvd = s.recv(1024)
        print('Received message from server: ' + recvd.decode('utf-8'))
    elif ch == 0:
        break
    else:
        print("Invalid choice\n")
s.close()