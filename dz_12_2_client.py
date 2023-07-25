import socket

def client():
    server_port = 54321

    number1 = int(input('Enter number 1: '))
    number2 = int(input('Enter number 2: '))
    while number2 != 0:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', server_port))
        client_socket.send(bytes(f'{number1} {number2}', encoding='UTF-8'))

        response = str(client_socket.recv(1024), encoding='UTF-8')
        client_socket.close()
    
        print(response)

        number1 = int(input('Enter number 1: '))
        number2 = int(input('Enter number 2: '))

client()