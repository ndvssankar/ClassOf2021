import os
import sys
import select
import signal
import time
def execute_script(uri):
    pr, cw = os.pipe()
    # cr, pw = os.pipe()
    stdin  = sys.stdin.fileno() # usually 0
    stdout = sys.stdout.fileno() # usually 1
    # st = ""
    pid = os.fork()
    # uri = uri.split("?")
    # args = None
    # if (len(uri) > 1):
    #     args = uri[1]

    if pid:
        # if args:
        # os.close(cr)
        print("from child cmd output is as follows")
        # pid, sts = os.waitpid(pid, 0)
        # throw away additional data [see bug #427345]
        # while select.select([sys.stdin], [], [], 0)[0]:
        #     if not input():
        #         break
        # if sts:
        #     print("CGI script exit status", sts)
        
        os.close(cw)
        # os.dup2(pr, stdin)
        # os.dup2(pw, stdout)
        # pw.write(args)
        # pw.close()
        # print(args)
        # os.close(pw)
        # os.close(pr)
        # os.close(cw)
        # time.sleep(1)
        # status = os.wait()
        # print(status)
        
        while :
            info = os.waitpid(pid, os.WNOHANG)
            print(info)
            if info[0] == 0:
                print("child terminated", pid)
                os.kill(pid, signal.SIGSTOP)
                return "Timedout error"
        
        # print("pr ", pr, stdin)
        # print ("Reading from client")
        # sys.stdin.flush()
        os.dup2(pr, stdin)
        res = "Output of command is : ", uri, "<br>"
        for line in sys.stdin:
            if line:
                # st = input()
                # st = os.read(pr, 1024)
                # print(type(st), len(st))
                print(line)
                # res = res + line + "<br>"
            
        os.close(pr)
        return res
        # return "expecting arguments to serve the request..."
    else:
        os.close(pr)
        # os.close(pw)
        # os.dup2(cr, stdin)
        os.dup2(cw, stdout)
        # sys.stdout.flush()
        # print("Executing in child....")
        # print(uri)
        # exec(open("forever.sh").read())
        print(os.getpid())
        # env = os.environ.copy()
        # cmd = "/bin/sh"
        # args = [cmd, "forever"]
        # cmd = "python3"
        # args = [cmd, "odd.py"]
        cmd = "/bin/ls"
        args = [cmd, "-la"]
        os.execvp(args[0], args)
        
        # sys.exit(1)
DOC_ROOT = "/Sankar/2021/ClassOf2021/Operating Systems/WebServer"
# execute_script(DOC_ROOT + "/scripts/odd.py?n=100")
print(execute_script("odd.py"))


# http://127.0.0.1:8888/bin/sh?filename=forever
# http://127.0.0.1:8888/bin/ls?args=-l
# http://127.0.0.1:8888/bin/du
# http://127.0.0.1:8888/bin/sh?filename=forever
# http://127.0.0.1:8888/bin/ls?args=-l
# http://127.0.0.1:8888/bin/du
# http://127.0.0.1:8888/bin/sh?filename=forever
# http://127.0.0.1:8888/bin/ls?args=-l
# http://127.0.0.1:8888/bin/du
