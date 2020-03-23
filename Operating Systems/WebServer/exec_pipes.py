stdin  = sys.stdin.fileno() # usually 0
stdout = sys.stdout.fileno() # usually 1

parentStdin, childStdout  = os.pipe() 
childStdin,  parentStdout = os.pipe() 
pid = os.fork()

def execute_script(uri):
    if processid:
        
    else:
        
    return st