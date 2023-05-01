import asyncio
import websockets
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

model = YOLO("yolov8n.pt")

x = ""

async def hello(websocket, path):
    global x
    try:
        x = await websocket.recv()
        print(f"Received: {x}")
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed unexpectedly")
    except Exception as e:
        print(f"Error: {e}")

async def listen_for_input():
    global x
    while True:
        if x == "0" or x:
            if x == "-1":
                print("Flushing input...")
                x = ""
            else:
                # do something with x
                try:
                    img = cv2.imread(x)
                    results = model.predict(source=img, save=True, save_txt=True)
                    with open("output.txt", "r") as f:
                        output = f.read()
                        await websocket.send(output)
                        print(f"Output sent: {output}")
                except Exception as e:
                    print(f"Error: {e}")
                x = ""
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        websockets.serve(hello, "localhost", 8765),
        listen_for_input()
    )

asyncio.run(main())
