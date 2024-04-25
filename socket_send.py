# import socket

# HOST = '192.168.86.122' # The server's hostname or IP address
# PORT = 6546 # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         message = input("Enter your message: ")
#         s.sendall(message.encode('utf-8'))
#         data = s.recv(1024)
#         print('Received from server:', data.decode('utf-8'))


import socket

HOST = '192.168.86.122'  # The server's hostname or IP address
PORT = 6546  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter your message: ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode('utf-8'))
