# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)  # Get the Tello drone's address

# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep=6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

def first_hoop():
    sendmsg('up 35')
    sendmsg('forward 200', 10)


def second_hoop():
    sendmsg('go 250 0 75 10', 10)


# def thirdHoop():


# def lastHoop():


print("\nKyle Rocco and Sullivan Abegg")
print("Program Name: Drone Comp ")
print("Date: 1.10.23")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')

try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff', 10)

        #firsthoop
        sendmsg('up 35' , 10)
        sendmsg('forward 175', 10)
        #secondhoop
        sendmsg('go 200 10 70 50', 10)

        sendmsg('cw 180', 10)
        sendmsg('curve -40 -25 0 -20 -300 0 30', 10)
        sendmsg('forward 225', 10)

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()