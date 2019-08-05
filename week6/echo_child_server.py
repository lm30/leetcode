import os
import sys
import socket # https://docs.python.org/3/library/socket.html

port = 4001
host = "localhost"
new_connections = 10

sock = socket.socket() # make socket
sock.bind((host, port)) # bind to the host:port
sock.listen(new connections) # will accept # unacceepted connections before will refuse new ones

num_forks = 5
# fork child processes
for i in range(num_forks):
	pid = os.fork() # parent gets pid of child upon calling this
	# pid in the child process would be 0
	if pid == 0:
		print "Accepting on socket " + host + ":" + port + " for child " + os.getpid()
		try:
			while True:
				conn, addr = sock.accept()

				pipelike = conn.makefile()
				pipelike.write('Child echo:')
				msg = pipelike.read()
				pipelike.write(msg)
				pipelike.close()
				print "Child echo: " + message.strip()
		except KeyboardInterrupt:
			sys.exit()

try:
	os.waitpid(-1, 0) # waits for children to exit
except KeyboardInterrupt:
	sys.exit()