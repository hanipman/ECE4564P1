# To install tweepy: sudo pip3 tweepy

import tweepy
import sys
from clientKeys import consumer_token, consumer_secret, access_token, access_secret

#auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
#auth.set_access_token(access_token, access_secret)
#api = tweepy.API(auth)

#search_result = api.search(search_hashtag, 2)
#for i in search_result:
#	print(i.text)

# https://gist.github.com/dideler/2395703
def getopts(argv):
	opts = {}
	while sys.argv:
		if sys.argv[0][0] == '-':
			opts[sys.argv[0]] = sys.argv[1]
		sys.argv = sys.argv[1:]
	return opts



myargs = getopts(sys.argv)
if '-s' in myargs:
	server_ip = myargs['-s']
if '-p' in myargs:
	server_port = myargs['-p']
if '-z' in myargs:
	socket_size = myargs['-z']
if '-t' in myargs:
	hashtag = myargs['-t']
print(server_ip)
print(server_port)
print(socket_size)
print(hashtag)

