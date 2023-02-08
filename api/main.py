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
import pupil_apriltags as apriltags

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
            with open('config/config.cfg', 'r') as f:
                config = configparser.ConfigParser()
                config.read_file(f)
                port = config['serial']['port']
                baudrate = config['serial']['baudrate']
                print(str(port), int(baudrate))
                ser_cnc = serial.serial_worker(str(port), int(baudrate))
                ser_cnc.start()
        except Exception as e:
            return {'error': str(e)}
    return {'success': True}
@app.post("/gcode")
async def gcode(gcode: str, wait: bool = False):
    global ser_cnc
    if ser_cnc is not None:
        print("gcode: ", gcode)
        ser_cnc.send(gcode)
        if wait:
            ser_cnc.to_device.join()
            
cap = None
@app.get("/image")
async def image():
    try:
        global cap
        if cap is None:
            with open('config/config.cfg', 'r') as f:
                config = configparser.ConfigParser()
                config.read_file(f)
                port = config['camera:main']['index']
                cap = cv2.VideoCapture(int(port))
        ret, frame = cap.read()
        if ret:
            #resize to 0.5
            resize_factor = 1
            frame = cv2.resize(frame, (0,0), fx=resize_factor, fy=resize_factor)
            return StreamingResponse(io.BytesIO(cv2.imencode('.jpg', frame)[1]), media_type="image/jpeg")
    except Exception as e:
        return {'error': str(e)}

#execute gcode macro

@app.post("/macros")
async def macros(macro: str):
    try:
        with open('config/config.cfg', 'r') as f:
            config = configparser.ConfigParser()
            config.read_file(f)
            commands = config['macros'][macro].split(',')
            print(commands)
            for command in commands:
                print("command: ", command)
                await gcode(command, True)
    except Exception as e:
        return {'error': str(e)}
    return {'success': True}
@app.post("/goto")
async def goto(position: str):
    try:
        with open('config/config.cfg', 'r') as f:
            config = configparser.ConfigParser()
            config.read_file(f)
            coordinates = config['mechanicalConstrains:Waypoints'][position].split(',')
            travel_height = config['mechanicalConstrains']['z-travel-height']
            Zspeed = config['mechanicalConstrains']['z-rate']
            XYspeed = config['mechanicalConstrains']['xy-rate']
            print('Zspeed: ', Zspeed)
            print('XYspeed: ', XYspeed)
            print('destination: x {}, y {}, z {}'.format(coordinates[0], coordinates[1], coordinates[2]))
            print('travel height: ', travel_height)
            await gcode('G90', True)#absolute coordinates
            await gcode('G0 Z' + str(travel_height) + ' F' + str(Zspeed), True) #move to travel height
            await gcode('G0 X' + str(coordinates[0]) + ' Y' + str(coordinates[1]) + ' F' + str(XYspeed), True) #move to destination
            await gcode('G0 Z' + str(coordinates[2]) + ' F' + str(Zspeed), True) #move to destination
    except Exception as e:
        return {'error': str(e)}
    return {'success': True}
            