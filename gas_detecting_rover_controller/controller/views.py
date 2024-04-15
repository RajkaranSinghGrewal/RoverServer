# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from controller.models import FlagModel
import time
import picamera
import io
import subprocess
import json
import requests     

ip_address = "http://192.168.50.25/"
# Create your views here.
def home(request):
    print("home")
#    request.session["forward_flag"] = False
 #   request.session["forward_right_flag"] = False
  #  request.session["forward_left_flag"] = False
  #  request.session["right_flag"] = False
  #  request.session["left_flag"] = False
  #  request.session["brake_flag"] = False
  #  request.session["reverse_right_flag"] = False
  #  request.session["reverse_left_flag"] = False
  #  request.session["reverse_flag"] = False
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
    print("right")
    obj = FlagModel.objects.get(id = 1)
    obj.right_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + "right",timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.right_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def left(request):
    print("left")
    obj = FlagModel.objects.get(id = 1)
    obj.left_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + "left",timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.left_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def forward(request):
    print("forward")
    obj = FlagModel.objects.get(id = 1)
    obj.forward_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + "forward",timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.forward_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        print("session forward flag", obj.forward_flag)
        return HttpResponse(status = 500)
def backward(request):
    print("backward")
    obj = FlagModel.objects.get(id = 1)
    obj.reverse_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + "backward",timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.reverse_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def forward_right(request):
    print("forward_right")
    obj = FlagModel.objects.get(id = 1)
    obj.forward_right_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + 'frward_right',timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.forward_right_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def forward_left(request):
    print("forward_left")
    obj = FlagModel.objects.get(id = 1)
    obj.forward_left_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + 'frward_left',timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.forward_left_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def reverse_left(request):
    print("reverse_left")
    obj = FlagModel.objects.get(id = 1)
    obj.reverse_left_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + 'reverse_left',timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.reverse_left_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def reverse_right(request):
    print("reverse_right")
    obj = FlagModel.objects.get(id = 1)
    obj.reverse_right_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + 'reverse_right',timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.reverse_right_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)
def brake(request):
    print("brake")
    obj = FlagModel.objects.get(id = 1)
    obj.brake_flag = True
    obj.save()
    try:
        response = requests.get(ip_address + '/break',timeout=5)
        if(response.status_code == 200):
            print("Success")
            obj.brake_flag = False
            obj.save()
            return HttpResponse(status = 200)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:", e)
        return HttpResponse(status = 500)
def data(request):
    obj = FlagModel.objects.get(id = 1)
    print("Session",vars(obj))
    if obj.right_flag:
        right(request)
        return HttpResponse(status = 500)
    if obj.left_flag:
        left(request)
        return HttpResponse(status = 500)
    if obj.forward_flag:
        forward(request)
        return HttpResponse(status = 500)
    if obj.forward_right_flag:
        forward_right(request)
        return HttpResponse(status = 500)
    if obj.forward_left_flag:
        forward_left(request)
        return HttpResponse(status = 500)
    if obj.reverse_left_flag:
        reverse_left(request)
        return HttpResponse(status = 500)
    if obj.reverse_right_flag:
        reverse_right(request)
        return HttpResponse(status = 500)
    if obj.reverse_flag:
        backward(request)
        return HttpResponse(status = 500)
    if obj.brake_flag:
        brake(request)
        return HttpResponse(status = 500)
    print("Data")
    try:
        response = requests.get(ip_address + '/data')
        if(response.status_code == 200):
            print("success")
            return JsonResponse(response.json(),safe=False)
        else:
            print("Failed")
            return HttpResponse(status = 500)
    except Exception as e:
        print("Error:",e)
        return HttpResponse(status = 500)

