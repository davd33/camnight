# Cameratesting

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)
camera.start_preview()

sleep(2)
camera.capture('foo.jpg')  # Alt + F4 um die Kamera zu stopen.

