from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import serial_asyncio
import time
import asyncio
import queue
import configparser
import os
import sys

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


