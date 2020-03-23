'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''

from socket import *

print ("Connecting to server...")

clientsocket = socket(AF_INET, SOCK_STREAM)
try:
	clientsocket.connect(('localhost', 10000))
except ConnectionRefusedError:
	print ("The connection was refused.")
	exit(0)
print("connected!")
message = "Hello"
guess = input("Enter your name: ")
message = message + " " + guess
clientsocket.send(message.encode('ascii'))
response = clientsocket.recv(1024)
print(response.decode('ascii'))

running = 1

while running:
	guess = input("Enter your guess: ")
	guessstring = "Guess: " + str(guess) + ""
	clientsocket.send(guessstring.encode('ascii'))

	response = clientsocket.recv(1024).decode('ascii')
	print (response)

	# Determine if the game is over
	if (response[0:7] == "Correct"):
		running = 0

# clientsocket.close()
