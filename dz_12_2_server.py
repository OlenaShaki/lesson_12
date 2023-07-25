import socket
import asyncio

async def add(numbers):
    await asyncio.sleep(0.5)
    return numbers[0] + numbers[1]

async def subtract(numbers):
    await asyncio.sleep(0.5)
    return numbers[0] - numbers[1]

async def multiply(numbers):
    await asyncio.sleep(0.5)
    return numbers[0] * numbers[1]




async def handle_connection(connection, address):
    loop = asyncio.get_event_loop()

    message = str(await loop.sock_recv(connection, 1024), encoding='UTF-8')
    numbers = [int(s) for s in message.split()]
    response = f'Add: {await add(numbers)}, subtract: {await subtract(numbers)}, multiply: {await multiply(numbers)}'
    await loop.sock_sendall(connection, bytes(response, encoding='UTF-8'))

    connection.close()

async def server():
    port = 54321

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    server_socket.listen(10)
    server_socket.setblocking(False)
    print('Server started')

    loop = asyncio.get_event_loop()

    while loop.is_running():
        connection, address = await loop.sock_accept(server_socket)
        print('    connection: ', address)

        asyncio.create_task(handle_connection(connection, address))
        
asyncio.run(server())