import socket


server = socket.socket()
server.bind(('', 5051))
server.listen()
connection,adress = server.accept()

print('Server is running!')
print('Waiting for clients...')

print(f'New connection from : {adress}')

while True:
    recieved = connection.recv(1024).decode()
    print(f'client : {recieved}')
    message = input(">>>: ")
    connection.send(message.encode())