'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''

import random
from socket import *

# Set up the socket

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('localhost', 10002))
serversocket.listen(5)


def handleclient(clientsocket, clientaddress):
	# Receive the client's greeting
	clientgreeting = clientsocket.recv(1024)
	welcomemessage = "READY"
	clientsocket.send(welcomemessage.encode('ascii'))
	# clientsocket.send(welcomemessage.encode())

	running = 1
	numberofguesses = 0
	# Generate a random number for the client to try and guess
	numbertoguess = generatenumber()
	print(numbertoguess)
	while running:
		guess = clientsocket.recv(1024)
		guessstring = guess.decode('ascii')
		print("Here", guessstring)
		guess = int(guessstring)
		numberofguesses += 1
		running = 1
		if (guess == numbertoguess):
			messagetosend = ("Correct! took " + str(numberofguesses) + " attempts to guess the secret")
			clientsocket.send(messagetosend.encode('ascii'))
			running = 0
		else:
			if guess > numbertoguess:
				messagetosend = ("HIGH")
			else:
				messagetosend = ("LOW")
			clientsocket.send(messagetosend.encode('ascii'))
	clientsocket.close()
	print("Connection closed.")

def generatenumber():
	return random.randrange(1, 20)

(clientsocket, clientaddress) = serversocket.accept()
print("Connection received from: ", clientaddress)
handleclient(clientsocket, clientaddress)
