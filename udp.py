#Server:
#echo server using UDP 
import socket
HOST="192.168.60.138"
PORT=65432
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((HOST, PORT))
print ("UDP server is running")
while True:
    data=s.recvfrom (1024)|
    message=data [0] 
    address=data [1]
    print (message.decode('utf-8')) 
    print (format (address))
    s.sendto (message, address)



#clint
#echo client using UDP 
import socket
HOST="192.168.60.138"
PORT=65432
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
while True:
    d1 = input ("Enter your message")
    s.sendto (d1.encode('utf-8'), (HOST, PORT))
    data= s.recvfrom (1024)
    print (data [0].decode('utf-8'))

