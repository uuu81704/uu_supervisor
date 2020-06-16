from picamera import PiCamera
import time
from time import sleep

camera = PiCamera()
camera.resolution = (1280,720) 
camera.iso = 800

count = 0

while count<3:
    #camera.start_preview()
    time_str = time.strftime("%Y%m%d-%H%M%S")
    camera.start_recording('/home/pi/Desktop/video {}.h264'.format(time_str))
    camera.wait_recording(5)
    camera.stop_recording()
    count = count + 1
    #camera.stop_preview()

