"""
Bluetooth server script to run on the Pi.
"""
import bluetooth
from picar_4wd import Ultrasonic, Pin, us
from picar_4wd.utils import getIP, cpu_temperature, cpu_usage
import picar_4wd as fc
import yaml
import argparse

hostMACAddress = "E4:5F:01:2D:6E:FB"
port = 0
backlog = 1
size = 1024


def get_stats():
    return f'Stats:\n\tIP Address:\t\t{getIP()}\n\tCPU Temp:\t\t{cpu_temperature()}\n\tCPU Usage:\t\t{cpu_usage()}\n\tDistance:\t\t{us.get_distance()}\n\n'


def forward():
    fc.forward(5)
    return 'Moving forward'


def backward():
    fc.backward(5)
    return 'Moving backward'


def left():
    fc.turn_left(5)
    return 'Turning left'


def right():
    fc.turn_right(5)
    return 'Turning right'


def stop():
    fc.stop()
    return 'Stopping the car'

def help():
    return "\n".join(commands)

commands = {
    'stats': get_stats,
    'forward': forward,
    'backward': backward,
    'left': left,
    'right': right,
    'stop': stop,
    'help': help
}

def run(host):
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((host, port))
    s.listen(backlog)
    us = Ultrasonic(Pin('D8'), Pin('D9'))
    print("Listening on port ", port)


    try:
        client, clientInfo = s.accept()
        print(f'Connected to {clientInfo[0]}')
        while 1:
            data = client.recv(size)
            if data:
                data_str = data.decode()
                if data_str in commands:
                    client.send(commands[data_str]().encode())
                else:
                    client.send('Unknown command'.encode())
    except Exception as e:
        print(f"Error {e}")
        print("Closing socket")
        client.close()
        s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client app for car control")
    parser.add_argument("--config", help="config file", default="config.yaml")
    args = parser.parse_args()
    with open(args.config) as f:
        config = yaml.safe_load(f)
    host = config['server']['address']
    run(host)