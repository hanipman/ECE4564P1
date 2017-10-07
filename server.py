import sys
import wolframalpha
from serverKeys import app_id

# https://gist.github.com/didler/2395703
def getopts(argv):
	opts ={}
	while sys.argv:
		if sys.argv[0][0] == '-':
			opts[sys.argv[0]] = sys.argv[1]
		sys.argv = sys.argv[1:]
	return opts

myargs = getopts(sys.argv)
if '-p' in myargs:
	server_port = myargs['-p']
if '-b' in myargs:
	backlog_size = myargs['-b']
if '-z' in myargs:
	socket_size = myargs['-z']

print(app_id)
print(server_port)
print(backlog_size)
print(socket_size)

# TODO
#
#question = ""
#
#client = wolframalpha.Client(app_id)
#res = client.query(question)
#answer = next(res.results).text

#print answer


