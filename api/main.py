from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

import time
import asyncio
import queue
import configparser
import os
import sys
import cv2 
import io
import lib.serial as serial

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


#-------------------General File System-------------------#

file_list_folder = 'files'

@app.get("/file_list")
async def file_list():
    files = os.listdir(file_list_folder)
    return files


@app.get("/file/{file_name}")
async def file(file_name: str):
    file_path = os.path.join(file_list_folder, file_name)
    return FileResponse(file_path)


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(os.path.join(file_list_folder, file.filename), "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    return {"filename": file.filename}

#-------------------Config File System-------------------#

config_list_folder = 'config'

@app.get("/config_list")
async def config_list():
    files = os.listdir(config_list_folder)
    return files

@app.get("/config/{file_name}")
async def config(file_name: str):
    file_path = os.path.join(config_list_folder, file_name)
    with open(file_path, 'r') as f:
        return f.read()

@app.post("/upload_config/")
async def create_upload_config(file: UploadFile = File(...)):
    with open(os.path.join(config_list_folder, file.filename), "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    return {"filename": file.filename}

ser_cnc = None
@app.post("/connect_serial")
async def connect_serial():
    global ser_cnc
    if ser_cnc is None:
        try:
            with open('config/serial.cfg', 'r') as f:
                config = configparser.ConfigParser()
                config.read_file(f)
                port = config['serial']['port']
                baudrate = config['serial']['baudrate']
                ser_cnc = serial.serial_worker(port, baudrate)
                ser_cnc.start()
        except Exception as e:
            return {'error': str(e)}
    
@app.post("/gcode")
async def gcode(gcode: str, wait: bool = False):
    global ser_cnc
    if ser_cnc is not None:
        ser_cnc.send(gcode)
        if wait:
            ser_cnc.to_device.join()
            
cap = None
@app.get("/image")
async def image():
    try:
        global cap
        if cap is None:
            with open('config/camera.cfg', 'r') as f:
                config = configparser.ConfigParser()
                config.read_file(f)
                port = config['camera']['port']
                cap = cv2.VideoCapture(int(port))
        ret, frame = cap.read()
        if ret:
            #resize to 0.5
            resize_factor = 1
            frame = cv2.resize(frame, (0,0), fx=resize_factor, fy=resize_factor)
            return StreamingResponse(io.BytesIO(cv2.imencode('.jpg', frame)[1]), media_type="image/jpeg")
    except Exception as e:
        return {'error': str(e)}
    