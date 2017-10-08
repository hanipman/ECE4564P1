# wolfram alpha: pip3 install wolframalpha
# espeak: sudo apt-get espeak

import sys
import wolframalpha
import os
import re
import subprocess
import socket
from serverKeys import app_id

# https://gist.github.com/didler/2395703
# Creates a dictionary that relates the commandline option to its argument
# does not account for empty spaces
def getopts(argv):
	opts ={}
	while sys.argv:
		if sys.argv[0][0] == '-':
			opts[sys.argv[0]] = sys.argv[1]
		sys.argv = sys.argv[1:]
	return opts

# argument error checking
# if the dictionary is empty, command is invalid
# if the specified argument is found in the dictionary, it is removed from it
# if the dictionary is not empty after removing all valid arguments, invalid arguments exist, so command is invalid
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

# binding sockets
host = '172.29.124.160'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, server_port))
print('[Checkpoint 01] Created socket at ' + host + ' at port ' + str(server_port))
s.listen(backlog_size)

# start while loop for client listening
while 1:
	# looking for clients
	print('[Checkpoint 02] Listening for client connections')
	client, address = s.accept()

	# parsing client info
	client_ip, client_port = str(address).split(",")
	client_ip = client_ip[2:-1]
	client_port = client_port[1:-1]
	print('[Checkpoint 07] Accepted client connection from ' + client_ip + ' on port ' + client_port)

	# obtaining question from client
	question = client.recv(int(socket_size))
	print('[Checkpoint 09] Received question: ' + str(question)[2:-1])

	# verifying wolframalpha api
	cl = wolframalpha.Client(app_id)

	# send question to wolframalpha
	print('[Checkpoint 10] Sending question to Wolframalpha: ' + str(question)[2:-1])
	res = cl.query(question)

	# parsing answer
	# if recieved more than one answer parses the first one
	answer = next(res.results).text
	if '|' in answer:
		answer = answer.split('|', 2)
		answer = answer[0] + answer[1].split('\n', 1)[0]
	print('[Checkpoint 11] Received answer from Wolframalpha: ' + answer)

	# parsing answer for espeak use
	parsed = re.sub('[^0-9a-zA-Z]+', ' ', answer)
	print('[Checkpoint 12] Speaking answer parsed for only Alphanumeric and Space characters: ' + parsed)
	cmd_beg = 'espeak -ven+m3 -k5 -s150 '
	cmd_end = ' --stdout | aplay'
	parsed = parsed.replace(" ", "_")

	# espeak
	with open(os.devnull, 'w') as devnull:
		subprocess.call(cmd_beg + parsed + cmd_end, stdout=devnull, stderr=devnull, shell=True)

	# send answer to client
	if answer:
		print('[Checkpoint 13] Sending answer: ' + answer)
		client.send(answer.encode())

	# cut off client connection
	client.close()
