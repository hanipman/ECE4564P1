# wolfram alpha: pip3 install wolframalpha
# espeak: sudo apt-get espeak

import sys
import wolframalpha
import os
import subprocess
import socket
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
if not myargs:
	print('No arguments found')
	sys.exit()
if '-p' in myargs:
	server_port = int(myargs['-p'])
	myargs.pop('-p', None)
if '-b' in myargs:
	backlog_size = int(myargs['-b'])
	myargs.pop('-b', None)
if '-z' in myargs:
	socket_size = myargs['-z']
	myargs.pop('-z', None)
if len(myargs.keys()) != 0:
	print('Invalid arguments')
	sys.exit()

host = '172.29.124.160'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, server_port))
print('[Checkpoint 01] Created socket at 0.0.0.0 at port ' + str(server_port))
s.listen(backlog_size)
while 1:
	print('[Checkpoint 02] Listening for client connections')
	client, address = s.accept()

	print('[Checkpoint 07] Accepted client connection from ' + str(client) + ' on port ' + str(address))
	question = client.recv(int(socket_size))

	print('[Checkpoint 09] Received question: ' + str(question))
	cl = wolframalpha.Client(app_id)

	print('[Checkpoint 10] Sending question to Wolframalpha: ' + str(question))
	res = cl.query(question)

	answer = next(res.results).text
	print('[Checkpoint 11] Received answer from Wolframalpha: ' + answer)

	parsed = answer
	print('[Checkpoint 12] Speaking answer parsed for only Alphanumeric and Space characters: ' + parsed)

	answer = answer.replace(" ", "_")
	cmd_beg = 'espeak -ven+f3 -k5 -s150 '
	with open(os.devnull, 'w') as devnull:
		subprocess.run(cmd_beg + answer, stdout=devnull, stderr=devnull, shell=True)

	if answer:
		answer = answer.replace("_", " ")
		print('[Checkpoint 13] Sending answer: ' + answer)
		client.send(answer.encode())

	client.close()
