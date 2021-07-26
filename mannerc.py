import socket
import authproc as encrypt

# Server
def clntconn(host, port, key):
    
    # Create socket object, omits Close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         
        # Connect using IPV4 AF
        sock.connect((host,port))
        
        # Encode string send bytes
        sock.sendall(str.encode(key)) 

        # Send data to socket
        data = sock.recv(1024)

    # Decode message and print
    print('Received: ', repr(data.decode()))

# Create connection
clntconn('127.0.0.1', 65432, encrypt.hash_key(encrypt.zest_key(),'This!Password¿IsSecure_♣'))