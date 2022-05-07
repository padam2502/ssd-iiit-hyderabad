import socket  
import sys
from _thread import *
from datetime import datetime


def threaded_client(connection):
    
    while True:
        data = connection.recv(2048)
        rev_str = data.decode('utf-8')[::-1]
        connection.send(str.encode(rev_str))
    connection.close()


if __name__ == "__main__":
    n = len(sys.argv)
    if n != 2:
        print("Invalid Arguments ")
    else:
        ThreadCount = 0
        soc = socket.socket()
        port = int(sys.argv[1])
        host = socket.gethostname()
        soc.bind((host, port))
        soc.listen(5)
        while 1:
            client_soc, address = soc.accept()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            print("Current Time =", current_time)
            start_new_thread(threaded_client, (client_soc, ))
            ThreadCount += 1
        soc.close()