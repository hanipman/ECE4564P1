# ECE4564P1
# Created: 10/1/2017
# Chris Boado (boadoct@vt.edu)
# Eric Chandler (chandler@vt.edu)
# Assignment 1 from Group 31 of ECE 4564 Network Applications
# "forty-two"

# Initialize server in commandline:
	python3 server.py -p <SERVER_PORT> -b <BACKLOG_SIZE> -z <SOCKET_SIZE>

# Initialize client in commandline:
	python3 client.py -s <SERVER_IP> -p <SERVER_PORT> -z <SOCKET_SIZE> -t "<HASHTAG>"

# Requires API keys for WolframAlpha and Tweepy in serverKeys.py and clientKeys.py, respectively.	

# imports:
#	sys 		- allows use of commandline arguments
#	wolframalpha 	- interface for WolframAlpha API
#	tweepy		- interface for Twitter API
#	os 		- allows use of operating system dependent functions
#	re		- regex for easy string parsing
#	subprocess	- used to send commands to shell
#	socket		- used to create network sockets
#	serverKeys	- contains WolframAlpha API keys
#	clientKeys	- contains Twitter API keys 

# Chris Boado 	- mainly worked on server.py, so implemeting wolfram and espeak
# Eric Chandler - mainly worked on client.py, so tweepy
# Obviously, helped each other out.
