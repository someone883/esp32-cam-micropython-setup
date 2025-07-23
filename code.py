import camera
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
