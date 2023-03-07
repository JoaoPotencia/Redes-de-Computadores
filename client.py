import socket


dest = '192.168.246.37'  
port = 10501


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((dest, port))
print(f'=== Conectando ao servidor {dest} : {port} ===')

while True:
    
    #envia a mensagem
    msg = input(': ')
    client.send(msg.encode())
    
    #recebe a mensagem enviada pelo servidor
    msg = client.recv(4096)
    
    #mostra a mensagem
    print(f'Server: {msg.decode()}')
