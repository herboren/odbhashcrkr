import socket, json

HOST = '127.0.0.1'
PORT = 65432
# Server
def clntconn(host, port, user, key):
    
    # Create socket object, omits Close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        jsonstr  = json.dumps([user, key])
        # Connect using IPV4 AF
        sock.connect((host,port))
        
        # Encode string send bytes
        #sock.sendall(str(ukey).encode('utf-8'))
        sock.sendall(jsonstr.encode('utf-8'))
 
        # Send data to socket
        data = sock.recv(1024)

    # Decode message and print
    print('Received: ', repr(data.decode()))

print('Password Requirement: a-z, A-Z, 0-9, !@#$%^&*()_+-=\n Example: Pass_word!24.')

# Create connection
clntconn(HOST, PORT,'Username_1','This()_+-=Password@IsSecure$&')