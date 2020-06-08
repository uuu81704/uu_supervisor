"""
record.py
1. 錄影
2. 儲存影片/每五秒一個檔名
3. 上傳google drive
study video to streaning
"""
#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import picamera
# 

camera = picamera.PiCamera()
camera.resolution = (1280, 960)
camera.iso = 800

camera.start_recording('video.h264')
camera.wait_recording(3)
camera.stop_recording()

