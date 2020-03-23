# first of all import the socket library 
import socket
import os

# next create a socket object 
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 1226

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode 
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or  
# an error occurs 
while True:
   # Establish connection with client. 
   conn, addr = s.accept()
   print 'Got connection from', addr
   req_data = conn.recv(1024)
   print("Request is : ", req_data)
   print (type(req_data))
#    l = req_data.split("\n")

#    print("Lins from here.... \n")
#    for s in l:
#        print (l)
   # send a thank you message to the client.
   http_response = b"""\
HTTP/1.1 200 OK
Content-Type: text/html


<h1>web server is under construction</h1>
"""
   for x in os.listdir('.'):
       http_response = http_response + '<a href = "' + x +'">' + x + '</a> <br>'

   # Close the connection with the client 
   conn.send(http_response)
   conn.send('Thank you for connecting')
   conn.close()
s.close()

