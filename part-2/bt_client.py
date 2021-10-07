"""
Bluetooth client script to run on the PC.
"""

import bluetooth

host = "E4:5F:01:2D:6E:FB" # The address of Raspberry PI Bluetooth adapter on the server.
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

instructions = \
'''
Commands:
    quit        Quit this program
    stats       Get stats about the Pi
    forward     Move forward
    backward    Move backward
    left        Turn left
    right       Turn right
    stop        Stop all wheels
'''


while 1:
    text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    sock.send(text)

    data = sock.recv(1024)
    print(data.decode())

sock.close()


