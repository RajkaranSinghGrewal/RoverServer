# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import time
import picamera
import io
import subprocess
import requests
     
# Create your views here.
def home(request):
    print("home")
    return render(request,'main.html')
def gen():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        camera.rotation = 180
        stream = io.BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n\r\n')
            stream.seek(0)
            stream.truncate()
def video_feed(request):
    print("video_feed")
    return StreamingHttpResponse(gen(),content_type='multipart/x-mixed-replace; boundary=frame')
def right(request):
    response = requests.get('http://10.0.0.25/right')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def left(request):
    response = requests.get('http://10.0.0.25/left')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def forward(request):
    response = requests.get('http://10.0.0.25/forward')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def backward(request):
    response = requests.get('http://10.0.0.25/backward')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def forward_right(request):
    response = requests.get('http://10.0.0.25/frward_right')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def forward_left(request):
    response = requests.get('http://10.0.0.25/frward_left')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def reverse_left(request):
    response = requests.get('http://10.0.0.25/reverse_left')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def reverse_right(request):
    response = requests.get('http://10.0.0.25/reverse_right')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return
def brake(request):
    response = requests.get('http://10.0.0.25/break')
    if(response.status_code == 200):
        print("Success")
    else:
        print("Failed")
    return

