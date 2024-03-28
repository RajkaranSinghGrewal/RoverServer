import time
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder, H264Encoder
from picamera2.outputs import FileOutput, FfmpegOutput
import io
import subprocess
from threading import Condition 

class VideoCamera:
    def __init__(self):
        # self.vs = PiVideoStream(resolution=(1920, 1080), framerate=30).start()
       # self.vs = PiVideoStream().start()
       # self.flip = flip # Flip frame vertically
       # self.file_type = file_type # image type i.e. .jpg
       # self.photo_string = photo_string # Name to save the photo
       # time.sleep(2.0)
        self.camera = picamera2.Picamera2()
        self.camera.configure(self.camera.create_video_configuration(main={"size":(640,480)}))
        self.streamOutput = StreamingOutput()
        self.camera.start()

     def get_frame(self):
       # frame = self.flip_if_needed(self.vs.read())
       # ret, jpeg = cv.imencode(self.file_type, frame)
       # self.previous_frame = jpeg
       # return jpeg.tobytes()
        self.camera.start()
        with self.streamOutput.condition:
            self.streamOutput.condition.wait()
            self.frame = self.streamOutput.frame

        return self.frame
        
class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()
    def write(self,buf):
        with self.condition:
            self.frame = buf
            self.condtion.notify_all()

