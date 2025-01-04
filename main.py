import asyncio
import google.generativeai as genai
import os
import socket
import telnetlib3

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def shell(reader: telnetlib3.TelnetReaderUnicode, writer: telnetlib3.TelnetWriterUnicode):
    print(f"CONNECT {reader} and {writer}")
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat()
    writer.write('\r\nWelcome to gemchat, type bye followed by return to hang up\r\n')
    while True:
        writer.write('\r\ngemini> ')
        line = await reader.readline()
        if line.strip() == 'bye':
            break
        response = await chat.send_message_async(line)
        writer.write(f'\r\n{response.text}\r\n')
        await writer.drain()
    writer.close()
    print(f"HANG UP {reader} and {writer}")

if __name__ == '__main__':
    port = int(os.getenv("PORT", "6023"))
    loop = asyncio.get_event_loop()
    coro = telnetlib3.create_server(port=port, shell=shell)
    print(f"Listening on {socket.gethostbyname(socket.gethostname())}:{port}")
    server = loop.run_until_complete(coro)
    loop.run_until_complete(server.wait_closed())
