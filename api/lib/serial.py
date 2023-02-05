import serial 
import os 
import threading
import time
import queue
import re

class serial_worker(threading.Thread):
    def __init__(self, port, baudrate):
        self.stop_event = threading.Event()
        self.port = port
        self.baudrate = baudrate
        self.to_device = queue.Queue()
        self.busy = False
        self._reader = None
        self._writer = None
        self.position = (0, 0, 0, 0)
        super().__init__()

    def connect(self):
        try:
            self._reader = serial.Serial(self.port, self.baudrate, timeout=1)
            print('connected')
            return True
        except Exception as e:
            print(e)
            return False

    def disconnect(self):
        self._reader.close()
        self._reader = None

    def is_busy(self):
        return self.busy

    def send(self, data):
        self.to_device.put(data)

    def is_connected(self):
        #check if the serial port is open and if the device is connected
        if self._reader is not None and self._reader.isOpen():
            return True
        print('serial port is not open')
        return False

    def temp_search(self, data):
        temp_regex_results = re.search('T:([^\s]+) \/([^\s]+) B:([^\s]+) \/([^\s]+) @:([^\s]+) B@:([^\s]+)', data.decode())
        if temp_regex_results:
            ht0_current_temp = temp_regex_results.group(1)
            ht0_target_temp = temp_regex_results.group(2)
            bed_current_temp = temp_regex_results.group(3)
            bed_target_temp = temp_regex_results.group(4)
            return True
        return False
    def position_search(self, data):
        position_regex_results = re.search('X:([^\s]+) Y:([^\s]+) Z:([^\s]+) E:([^\s]+)', data.decode())
        if position_regex_results:
            x = float(position_regex_results.group(1))
            y = float(position_regex_results.group(2))
            z = float(position_regex_results.group(3))
            e = float(position_regex_results.group(4))
            self.position = (x, y, z, e)
            return True
        return False
    def reader(self):
        data = self._reader.readline()
        if not data == b'':
            
            found = self.position_search(data) or self.temp_search(data)
            if not found:
                print('received: ', data.decode())
        if b'ok' in data:
            self.busy = False
            if self.to_device.empty():
                self.to_device.task_done()
        if b'echo:busy: processing' in data:
            # clear_output()
            # display('busy: processing')
            self.busy = True
        
    def writer(self):
        if not self.busy and not self.to_device.empty():
            data = self.to_device.get()
            data = data + '\r'
            self._reader.write(data.encode())
            self._reader.flush()
            self.busy = True
    def run(self):
        print('thread started')
        if self.connect():
            while not self.stop_event.is_set():
                self.writer()
                self.reader()
        print('thread stopped')
        self.disconnect()
        self.stop_event.clear()
        self.to_device.queue.clear()
