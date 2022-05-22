#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('./picture_'+datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")+'.jpg')
camera.stop_preview()
