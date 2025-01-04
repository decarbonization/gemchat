import asyncio
import os
import socket
import telnetlib3

async def shell(reader: telnetlib3.TelnetReader, writer: telnetlib3.TelnetWriter):
    writer.write('\r\nWould you like to play a game? ')
    inp = await reader.read(1)
    if inp:
        writer.echo(inp)
        writer.write('\r\nThey say the only way to win '
                     'is to not play at all.\r\n')
        await writer.drain()
    writer.close()

if __name__ == '__main__':
    port = int(os.getenv("PORT", "6023"))
    loop = asyncio.get_event_loop()
    coro = telnetlib3.create_server(port=port, shell=shell)
    print(f"Listening on {socket.gethostbyname(socket.gethostname())}:{port}")
    server = loop.run_until_complete(coro)
    loop.run_until_complete(server.wait_closed())
