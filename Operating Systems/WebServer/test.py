import sys
import os
import contextlib
from io import StringIO

def execute (uri):
	r, w = os.pipe()
	processid = os.fork()
	if processid:
		os.close(w)
		r = os.fdopen(r)
		st = r.read()
		print ("From Child :: " + st)
		r.close()
		return st
	else:
		os.close(r)
		w = os.fdopen(w, 'w')
		# f = open(docroot + uri, 'rb')

		tokens = uri.split("?")
		tokens = tokens[1].split("=")
		print(tokens)
		with stdoutIO() as s:
			sys.argv = tokens
			exec(open("./scripts/odd.py").read())
		w.write("Hello from child to parent" + s.getvalue())
		w.close()

@contextlib.contextmanager
def stdoutIO(stdout = None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

execute("uri?n=9")