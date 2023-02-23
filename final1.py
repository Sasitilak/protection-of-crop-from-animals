import asyncio
import websockets

async def hello(websocket, path):
    x = ""
    try:
        while True:
            x = await websocket.recv()
            if x == "-1":
                print("End signal received.")
                break
            print(f"Received: {x}")
            # place your code here
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed unexpectedly")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        print("Waiting for input...")
        while True:
            await asyncio.sleep(1)

asyncio.run(main())
