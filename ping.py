import subprocess

def ping(host):

    # arguement for number of packets to be sent
    param = '-n'

    #creates command using ping as command and -n arguement to send 1 packet to the specified host
    command = ['ping', param, '1', host]

    # the command is fed into command prompt and returns code
    return subprocess.call(command) == 0

#specify host to ping
host = input("Enter Host Name : ")

#if the return code is true i.e 0 run statement
if ping(host):
    print("Host Is Awake")

#if ping fails run statement
else:
    print("Host Is Unreachable")
