"""
Playball.py is a CLI for Gmusic!
"""

from gmusicapi import Webclient
import getpass
import sys


def connect(api, username, password):
	"""
	Opens a session with Gmusic. Returns success.
	"""
	return api.login(username, password)


def main():
	api = Webclient()
	loggedIn = connect(api, raw_input('Username: '), getpass.getpass('Password: '))

	if not loggedIn:
		print "Authorization unsuccessful"
		sys.exit(0)
	else:
		print "Authorization successful!"

	print api.get_all_songs()[0]

if __name__ == '__main__':
	main()