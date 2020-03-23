import socket
import re
import os
import io
import mimetypes
from datetime import datetime
import traceback
import sys
import contextlib
import urllib
import html
# import html.client
from io import StringIO

DOC_ROOT = "/Sankar/2021/ClassOf2021/Operating Systems/Web Server"
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
        print("REquest :::::::::::: ", http_request)
        http_response = handle_request(http_request)
        print("RESEponse :::::::::: ", http_response)
        conn.send(http_response.encode())
        conn.close()

'''
handle http request and return response data
'''
def handle_request(request):
    # http_response = ""
    request = request.decode()
    flag = re.match("GET ", request)
    file_data = ""
    
    if (flag):
        uri = re.split(" ", request)[1]
        # uri = uri[1:]
        print ("URI : " , uri)
    

    # if (uri == "favicon.ico"):
    #     pass
        # prepare_response("200", "OK", "text/palin", "<link: rel='icon' href='#';,' type='image/x-icon'>") 
        # prepare_response("200", "OK", "text/palin", "<link rel='icon' href='data:,'>")
        # prepare_response("200", "OK", "text/plain", ' "Link:" + rel=" + 'shortcut icon' + "href=" + '#')
        # res.writeHead(200, "OK", 'text/plain', {'Link': 'rel="shortcut icon" href="#"'} );
        # return http_response
    # if (uri != "favicon.ico"):
    if request.find("scripts") != -1:
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

def list_direcctory(dir_path):
    displaypath = ""
    path = ""
    try:
        list = os.listdir(dir_path)
    except OSError:
        return prepare_response("404", "File Not Found", "text/plain", "No permission to list directory")
    list.sort(key=lambda a: a.lower())
    r = []
    # try:
    #     displaypath = urllib.parse.unquote(self.path, errors='surrogatepass')
    # except UnicodeDecodeError:
    #     displaypath = urllib.parse.unquote(path)
    displaypath = html.escape(displaypath, quote=False)
    enc = sys.getfilesystemencoding()
    title = 'Directory listing for %s' % displaypath
    r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                '"http://www.w3.org/TR/html4/strict.dtd">')
    r.append('<html>\n<head>')
    r.append('<meta http-equiv="Content-Type" '
                'content="text/html; charset=%s">' % enc)
    r.append('<title>%s</title>\n</head>' % title)
    r.append('<body>\n<h1>%s</h1>' % title)
    r.append('<hr>\n<ul>')
    for name in list:
        print ("OS Path : " , os.path)
        fullname = os.path.join(path, name)
        displayname = linkname = name
        # Append / for directories or @ for symbolic links
        if os.path.isdir(fullname):
            displayname = name + "/"
            linkname = name + "/"
        if os.path.islink(fullname):
            displayname = name + "@"
            # Note: a link to a directory displays with @ and links with /
        r.append('<li><a href="%s">%s</a></li>'
                % (urllib.parse.quote(linkname,
                                        errors='surrogatepass'),
                    html.escape(displayname, quote=False)))
    r.append('</ul>\n<hr>\n</body>\n</html>\n')
    encoded = '\n'.join(r).encode(enc, 'surrogateescape')
    f = io.BytesIO()
    f.write(encoded)
    f.seek(0)
    output = ""
    for s in r:
        output = output + " " + s
    return prepare_response("200", "Directory Listing", "text/plain", output)



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
    r, w = os.pipe()
    processid = os.fork()
    st = ""
    # print("Execute script " , uri)
    if processid:
        os.close(w)
        r = os.fdopen(r)
        st = r.read()
        # print ("From Child :: " + st)
        r.close()
    else:
        os.close(r)
        w = os.fdopen(w, 'w')
        flag = uri.find("?")
        if flag != -1:
            tokens = uri.split("?")
            tokens = tokens[1].split("=")
            sys.argv = tokens
        # print("here 11.....")
        with stdoutIO() as s:
            exec(open(DOC_ROOT + "scripts/odd.py").read())
        w.write("Hello from child to parent" + s.getvalue())
        w.close()
    return st

@contextlib.contextmanager
def stdoutIO(stdout = None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


sock = init('127.0.0.1', 1236)
start_server(sock)
serve_clients(sock)

#list_direcctory("./")

