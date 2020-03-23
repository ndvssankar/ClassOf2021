import socket
import re
import os
import mimetypes
from datetime import datetime
import traceback
import sys
import contextlib
from io import StringIO
from _thread import *
import threading

DOC_ROOT = "/Sankar/ClassOf2021/Operating Systems/WebServer"
cache_lst = {}
enable_directory_browsing = True

'''Initialize the webserver with a port and IP
and return socket
@params IP, Port
'''
def init(IP, port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   sock.bind((IP, port))
   print ("socket binded to %s" %(port))
   return sock

def cache_hit(uri):
    for t in cache_lst:
        if t[0] == uri:
            cache_lst.remove(t)
            cache_lst.append(t)
            return t[1]
    return None

def cache_miss(uri, http_response):
    if len(cache_lst) < 10:
        cache_lst.append((uri, http_response))
    else:
        cache_lst.remove()

'''
start server to listen for connections
@params socket
'''
def start_server(socket):
   socket.listen(1)
   print ("socket is listening")
    
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

        if http_request.decode().find("favicon.ico")!=-1:
            conn.close()
            continue
        uri = get_uri(request)
        if uri in cache:
            return cache[uri]
        else:
            print("REquest :::::::::::: ", http_request)
            http_response = handle_request(http_request)
            if cache.size() < 5:
                cache[uri] = http_response
            else:

            print("RESEponse :::::::::: ", http_response)
        conn.send(http_response.encode())
        conn.close()

def get_uri(request):
    if (flag):
        uri = re.split(" ", request)[1]
        # uri = uri[1:]
        print ("URI : " , uri)
    return uri

'''
handle http request and return response data
'''
def handle_request(request):
    # http_response = ""
    request = request.decode()
    flag = re.match("GET ", request)
    file_data = ""
    
    uri = get_uri(request)

    if (uri == "favicon.ico"):
        pass
        # prepare_response("200", "OK", "text/palin", "<link: rel='icon' href='#';,' type='image/x-icon'>") 
        # prepare_response("200", "OK", "text/palin", "<link rel='icon' href='data:,'>")
        # prepare_response("200", "OK", "text/plain", ' "Link:" + rel=" + 'shortcut icon' + "href=" + '#')
        # res.writeHead(200, "OK", 'text/plain', {'Link': 'rel="shortcut icon" href="#"'} );
        # return http_response
    # if (uri != "favicon.ico"):
    elif request.find("scripts") != -1:
        output = execute_script("/" + uri)
        print("Output is : " , output , " :: ", type(output))
        http_response = prepare_response("200", "OK", "text/html", output)
    elif(uri=="" or uri == "/"):
        uri = DOC_ROOT + "/"
        if(os.path.isdir(uri)):
            file_data = list_direcctory(uri)
            http_response = prepare_response("200", "OK", "text/html", str(file_data))
        elif(os.path.isfile(uri)):
            mime = mimetypes.MimeTypes().guess_type(uri)[0]
            mime = str(mime)
            f = open(DOC_ROOT + uri, "rb")
            file_data = f.read()
            f.close()
            http_response = prepare_response("200", "OK", mime, file_data)
        else:
            http_response = prepare_response("404", "File Not Found", "text/html", "<h1>File Not Found</h1>")
    return http_response
      
def validate_request(request):
   return request == 'GET'

def list_direcctory(dirpath):
    parent = dirpath.split("/")[-2:-1]
    if(len(parent)>0):
        parent=parent[0]
    else:
        parent = "../"
    response = """
            <html>
            <head>
            <title>Index of </title>
            </head>
            <body>
            <h1>Index of /"""+dirpath+"""</h1>
            <table>
            <th>Name</th><th>Size</th><th>Last Modified</th>
        """
    try:
        response=response+"<tr><td><a href='./"+parent+"'>..</a></td><td></td><td></td></tr>"      
        for filename in os.listdir(dirpath):
            info = os.stat(dirpath+"/"+filename)
            dt_object = datetime.fromtimestamp(info.st_atime)
            response=response+"<tr><td><a href='/"+dirpath+"/"+filename+"'>"+filename+"</a></td><td>"+str(round(info.st_size/1024.0,2))+"K</td><td>"+str(dt_object)+"</td></tr>"
    except Exception:
         traceback.print_exc()
         return ""
    response = response+"""       
            </table>
            </body></html>
        """  
    return response

def prepare_response(status_code, status_message, content_type, message):
    # msg = message.decode()
    # print(msg , " Here..... ", type(msg))

    print("contnt type :"+content_type)   
    response = 'HTTP/1.1 ' + status_code + " " + status_message + '\r\n'
    response = response +'Content-Type: '+content_type+'\r\n'
    response = response +'Content-Length: '+str(len(message))+'\r\n'      
    response = response+'\r\n'
    response = response + message
    print("REsonse is : " , response)
    # response = response.encode()
    return response


def execute_script(uri):
    pr, cw = os.pipe()
    cr, pw = os.pipe()
    stdin  = sys.stdin.fileno() # usually 0
    stdout = sys.stdout.fileno() # usually 1

    pid = os.fork()
    if pid:
        os.close(cr)
        pw = os.fdopen(pw, "w")
        parent_writes = "n=10"
        pw.write(parent_writes)
        pw.close()

        os.close(cw)
        pr = os.fdopen(pr)
        str = pr.read()
        print("From chold" , str)

    else:
        os.close(pw)
        os.dup2(cr, stdin)
        os.dup2(cw, stdout)
        
        stdin = os.fdopen(stdin)
        cw = os.fdopen(stdout, "w")
        exec(open("scripts/odd.py").read())

sock = init('127.0.0.1', 1236)
start_server(sock)
serve_clients(sock)

#list_direcctory("./")

