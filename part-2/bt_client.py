"""
Bluetooth client script to run on the PC.
"""

import bluetooth
import argparse
import yaml

host = "E4:5F:01:2D:6E:FB" # The address of Raspberry PI Bluetooth adapter on the server.
port = 1

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

def run(host):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print("Connecting")
    sock.connect((host, port))
    while 1:
        text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        sock.send(text)

        data = sock.recv(1024)
        print(data.decode())

    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client app for car control")
    parser.add_argument("--config", help="config file", default="config.yaml")
    args = parser.parse_args()
    with open(args.config) as f:
        config = yaml.safe_load(f)
    host = config['server']['address']
    run(host)