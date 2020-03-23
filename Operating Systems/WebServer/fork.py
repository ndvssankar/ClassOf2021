import os 
from math import *

def parent_child(): 
    n = os.fork()
    r, w = os.pipe()

    # n greater than 0  means parent process 
    if n > 0:
        os.close(r)
        print("Parent process and id is : ", os.getpid()) 
        #r = os.fdopen(r)
        print("From child  : ", r.read())
        # os.close(r)
        
  
    # n equals to 0 means child process 
    else:
        # exec('', {'fact': factorial})
        print("Child process and id is : ", os.getpid()) 
        fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
        os.dup2(0, fd)
        
        exec(open("odd.py").read())
        # os.lseek(fd, 0, 0)
        # str = os.read(fd, 100)
        # print ("Read String is : ", str)
        # os.close( fd )

        # #s = os.popen("python odd.py")
        # # text = b"Hello child process"
        # # os.write(w, bytes(s))

        # # # print var
        # # r = os.fdopen(r)
        # # s = r.read()
        
        # # print("Hello " , s.read())
        # print("Child process and id is : ", os.getpid()) 

          
# Driver code 
parent_child()