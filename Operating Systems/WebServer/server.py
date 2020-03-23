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

DOC_ROOT = "/Sankar/2021/ClassOf2021/Operating Systems/WebServer"
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

'''
start server to listen for connections
@params socket
'''
def start_server(socket):
   socket.listen(5)
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
        http_request = conn.recv(1024)
        if http_request.decode().find("favicon.ico")!=-1:
            conn.close()
            continue
        # print("REquest :::::::::::: ", http_request)
        # used for iterative server....
        if (http_request.decode() != ""):
            http_response = handle_request(http_request)

            # used for conncurency...
            # thread = threading.Thread(Target=serve_clients, addr)
            # thread.start()
            # print("RESEponse :::::::::: ", http_response)
            conn.send(http_response)
            conn.close()

'''
handle http request and return response data
'''
def handle_request(request):
    # http_response = ""
    request = request.decode()
    if (request != ""):
        flag = re.match("GET ", request)
        file_data = ""

        # print ("Request is : ", request)
        
        uri = request.split(" ")[1]
        print ("URI : " , uri)
        if (flag):
            uri = re.split(" ", request)[1]
            print ("URI : " , uri)
        
            if (uri == "favicon.ico"):
                pass
            if (uri != "favicon.ico"):
                http_response = prepare_response("404", "File Not Found", "text/html", "<h1>File Not Found</h1>".encode())
                if uri == "":
                    uri = "/"
                elif re.match("/scripts/odd.py", uri):
                    output = execute_script(DOC_ROOT + uri)
                    # print (output, " is the output")
                    if (output != "expecting arguments to serve the request..."):
                        return prepare_response("200", "OK", "text/html", output.encode())
                    else:
                        return prepare_response("409", "Provide arguments to serve the request in the uri", "text/html", output.encode())
                elif re.match("/bin", uri):
                    output = execute_script("." + uri)
                    if (output != "expecting arguments to serve the request..."):
                        return prepare_response("200", "OK", "text/html", output.encode())
                    else:
                        return prepare_response("409", "Provide arguments to serve the request in the uri", "text/html", output.encode())
                elif(os.path.isdir(DOC_ROOT + uri)):
                    if  enable_directory_browsing:
                        file_data = list_direcctory(uri)
                        http_response = prepare_response("200", "OK", "text/html", file_data.encode())
                    else:
                        http_response = prepare_response("200", "OK", "text/html", "<h1>Webserver Under construction</h1>".encode())
                elif(os.path.isfile(DOC_ROOT + uri)):
                    # print ("URI is : " + uri + "in files.....")
                    # print ("URI with path is : " + DOC_ROOT + uri)
                    mime = mimetypes.MimeTypes().guess_type(DOC_ROOT + uri)[0]
                    mime = str(mime)
                    
                    f = open(DOC_ROOT + uri, "rb")
                    file_data = f.read()
                    f.close()
                    http_response = prepare_response("200", "OK", mime, file_data)
                else:
                    http_response = prepare_response("404", "File Not Found", "text/html", "<h1>File Not Found</h1>".encode())
                return http_response
        else:
            # print ("Bad request......")
            return prepare_response("405", "Bad Request", "text/html", "<h1>Bad request method</h1>".encode())

      
def validate_request(request):
   return request == 'GET'

def list_direcctory(dirpath):
    if (dirpath[-1] == "/"):
        dirpath = dirpath[0:len(dirpath)-1]
    parent = dirpath.split("/")[0:-1]
    print("parent : ", parent)
    parent = "/".join(parent)
    print("parent : ", parent)
    if (parent == ""):
        parent = "/"
    print("parent : ", parent, dirpath)
    response = """
            <html><head><title>Index of </title></head><body>
            <h1>Index of """+dirpath+"""</h1>
            <table>
            <th>Name</th><th>Size</th><th>Last Modified</th>
        """
    try:
        response = response + "<tr><td><a href='"+parent+"'>..</a></td><td></td><td></td></tr>"
        print("cwd : ", DOC_ROOT + dirpath)
        for filename in os.listdir(DOC_ROOT + dirpath):
            info = os.stat(DOC_ROOT+dirpath + "/" + filename)
            dt_object = datetime.fromtimestamp(info.st_mtime)
            # print("DirPath is : " + dirpath + filename)
            # print ("'/"+dirpath+"/"+filename+"'")
            # response=response+"<tr><td><a href='/"+dirpath+"/"+filename+"'>"+filename+"</a></td><td>"+str(round(info.st_size/1024.0,2))+"K</td><td>"+str(dt_object)+"</td></tr>"
            if dirpath == "/":
                response=response+"<tr><td><a href='/"+filename+"'>"+filename+"</a></td><td>"+str(round(info.st_size/1024.0,2))+"K</td><td>"+str(dt_object)+"</td></tr>"
            else:
                response=response+"<tr><td><a href='"+os.path.join(dirpath, filename)+"'>"+filename+"</a></td><td>"+str(round(info.st_size/1024.0,2))+"K</td><td>"+str(dt_object)+"</td></tr>"
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

    # print("contnt type :" + content_type)
    response = 'HTTP/1.1 ' + status_code + " " + status_message + '\r\n'
    response = response +'Content-Type: '+content_type+'\r\n'
    response = response +'Content-Length: '+str(len(message))+'\r\n'  
    response = response+'\r\n'
    # print("Message is : " , message, " : " ,message.encode())
    response = response.encode() + message
    # print("REsonse is : " , response)
    # response = response.encode()
    return response


def execute_script(uri):
    # print(uri, " in executing scripts")
    pr, cw = os.pipe()
    cr, pw = os.pipe()
    stdin  = sys.stdin.fileno() # usually 0
    stdout = sys.stdout.fileno() # usually 1
    st = ""
    pid = os.fork()
    uri = uri.split("?")
    fname = uri[0]
    # print("fname is : " + fname)
    args = None
    if (len(uri) > 1):
        args = uri[1]

    if pid:
        if args:
            os.close(cr)
            os.close(cw)
            # os.dup2(pr, stdin)
            os.dup2(pw, stdout)
            # pw.write(args)
            # pw.close()
            print(args)
            os.close(pw)
            # os.close(pr)
            # os.close(cw)
            os.dup2(pr, stdin)
            # print ("Reading from client")
            # st = input()
            res = "Output of the uri:", fname
            for line in sys.stdin:
                res = res + line + "<br>"

            print("From chold" , st)
            # os.close(pr)
            return st
        return "expecting arguments to serve the request..."

    else:
        os.close(pr)
        os.close(pw)
        os.dup2(cr, stdin)
        os.dup2(cw, stdout)
        # print("Executing in child....")
        args = input()
        args.insert(0, fname)
        execvp(args[0], args)
        # exec(open(fname).read())
        # sys.exit(1)

sock = init('127.0.0.1', 1239)
start_server(sock)
serve_clients(sock)
