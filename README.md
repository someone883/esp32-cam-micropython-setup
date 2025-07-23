# Esp32-cam-micropython-setup
## Prerequisites:
* Python (any version)
## Installing libs:
* Install esptool with `pip install esptool` or `pip3 install esptool`
* Download this repo and extract it https://github.com/lemariva/micropython-camera-driver
## Image esp32 cam with micropython
* `cd` your way to the extracted folder
* Run these 2 lines in command prompt
* Note: replace "USB0" with whatever the port your esp32 cam is connected to
``` 
esptool.py --chip esp32 --port USB0 erase-flash
esptool.py --chip esp32 --port USB0 write_flash -z 0x1000 micropython_camera_feeeb5ea3_esp32_idf4_4.bin
```
## Test code
```import camera
import network
import time


try:
    print('Taking a photo')
    camera.init(0,format=camera.JPEG)
    buffer=camera.capture()
    print(len(buffer))
    time.sleep(0.25)
    file_path="captured_image.jpg"
    file=open(file_path,"w")
    file.write(buffer)
    file.close()
except Exception as e:
    print("an issue occured", e)
finally:
    print("deinit camera and wifi")
    camera.deinit()
```
* This code should take a picture and save it to the esp32 cam
