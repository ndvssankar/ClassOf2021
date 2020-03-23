import os, sys, random

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