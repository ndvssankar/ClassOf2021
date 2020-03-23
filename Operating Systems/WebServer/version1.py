'''Initialize the webserver with a port and IP
and return socket
@params IP, Port
'''
def init(IP, port):
	s = socket.socket()
    s.bind(('', port))
    print "socket binded to %s" %(port)
    return s


'''
start server to listen for connections
@params socket
'''
def start_server(socket):
	socket.listen(10)
    print "socket is listening"
    
'''
to accept the connection, read request and send response
@params socket
'''
def serve_clients(socket):
    # a forever loop until we interrupt it or  
    # an error occurs 
    while True:
        # Establish connection with client. 
        conn, addr = socket.accept()
        print 'Got connection from', addr
        http_request  = conn.recv(1024)
        http_response = handle_request(http_request)
        conn.send(http_response)

'''
handle http request and return response data
'''
def handle_request(request):
	http_response = b"""\
HTTP/1.1 200 OK
Content-Type: application/pdf


<h1>web server is under construction</h1>
"""