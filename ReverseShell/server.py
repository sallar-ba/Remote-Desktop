# Hacker/User Computer

# Two Computer Can Connect To Each other
import socket
# Terminal Command in Python
import sys


# Create a Socket (connect to computers)
def createSocket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket() # Creating a Socket
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

# Binding the Socket and Listening for Connections