import ssl, socket
data = "eee"
HOST, PORT = '127.0.0.1', 443
for i in range(100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2)
    wrappedSocket.connect((HOST, PORT))
    wrappedSocket.send(data.encode('ascii'))
    print(wrappedSocket.recv(1280))
    wrappedSocket.close()
    sock.close()
    
