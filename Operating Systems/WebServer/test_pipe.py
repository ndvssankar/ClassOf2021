# Python program to explain os.pipe() method  
  
# importing os module  
import os 
import sys
# Create a pipe 
pr, cw = os.pipe()
cr, pw = os.pipe()
stdin  = sys.stdin.fileno() # usually 0
stdout = sys.stdout.fileno() # usually 1
    
# The returned file descriptor r and w 
# can be used for reading and 
# writing respectively. 
  
# We will create a child process 
# and using these file descriptor 
# the parent process will write  
# some text and child process will 
# read the text written by the parent process 
  
# Create a child process 
pid = os.fork() 
  
# pid greater than 0 represents 
# the parent process 
if pid > 0: 
  
    # This is the parent process  
    # Closes file descriptor r 
    # os.close(pr)
    os.close(cw)
    os.close(cr)
    # print("Parent process is writing") 
    
    os.dup2(pw, stdout)
    text = "n=10"
    print(text)
    os.close(pw)

    os.dup2(pr, stdin)
    st = input()
    print(st)

    # print("Written text:", text.decode()) 
else:
    # This is the parent process  
    # Closes file descriptor w 
    # os.close(pw)
    # os.close(pr)
    # Read the text written by parent process 
    # print("\nChild Process is reading") 
    # print(open("scripts/odd.py").read())
    os.dup2(cr, stdin)
    os.dup2(cw, stdout)
    exec(open("scripts/odd.py").read())
