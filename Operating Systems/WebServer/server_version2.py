import socket
import re
import os

DOC_ROOT = "/Sankar/2021/ClassOf2021/Operating Systems/MyProject"
enable_directory_browsing = false


'''Initialize the webserver with a port and IP
and return socket
@params IP, Port
'''
def init(IP, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((IP, port))
   print "socket binded to %s" %(port)
   return s

'''
start server to listen for connections
@params socket
'''
def start_server(socket):
   socket.listen(1)
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
      # print 'Got connection from', addr
      http_request  = conn.recv(1024)
      http_response = handle_request(http_request)
      conn.send(http_response)
      conn.close()

'''
handle http request and return response data
'''
def handle_request(request):
   # print("Request data is : ")
   # print(type(request))
   flag = re.match("GET ", request)
   file_data = ""
   if (flag):
      uri = re.split(" ", request)[1]
      if (uri != "/favicon.ico"):
         print("URL is : " + uri)
         if uri in ".html":
            f = open(DOC_ROOT + uri, "r")
            file_data = f.read()
         # elif uri in ".py":

            
   #    http_response = b"""\
   # HTTP/1.1 200 OK
   # Content-Type: text/html


   # <h1>web server is under construction</h1>
   # """ + file_data
      return http_response
   else:
      return prepare_response(400, "Bad Request", "text/html", "We found a bad request")
   #    http_response = b"""\
   # HTTP/1.1 400 Bad Request
   # Content-Type: text/html

   # <h1>We found a bad request</h1>
   # """
   # return http_response
      
def validate_request(request):
   return request == 'GET'

def prepare_response(status_code, status_message, content_type, message):
   return b"""\
   HTTP/1.1 """ + status_code + " " + status_message + """
   Content-Type: """ + content_type + """

   """ + message


sock = init('127.0.0.1', 1236)
start_server(sock)
http_response = serve_clients(sock)
print(http_response)
