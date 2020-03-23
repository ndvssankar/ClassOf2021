import socket
HOST = '10.10.8.142'       # The remote host
PORT = 8888     # The same port as used by the server
while True:    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # data = input()
    data = "Hello World"
    s.send(data.encode())
    data = s.recv(1024)
    s.close()
print ('Received', data)