#!/usr/bin/env python
import os
import sys
import netifaces
import requests
import time


def get_ip_address(interface='wlan0'):
    try:
        addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if addresses:
            return addresses[0]['addr']
        else:
            return None
    except ValueError as e:
        print('Error:',e)
        return None
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gas_detecting_rover_controller.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    ip_address = None
    while ip_address == None:
        ip_address = get_ip_address()
    data = {'ip_address':str(ip_address) + '.'}
    print(data)
    print("RESETTING")
    try:
        for i in range(0,5):
            print(".")
            time.sleep(1)
        response = requests.get('http://10.0.0.25/ip_configure',data=data)
        print("response:",response.status_code)
        #while response.status_code != 200:
        #    print("Error: ",response.status_code)
        #    time.sleep(10)
        #    response = requests.post('http://10.0.0.25/ip_configure',data=data)
    except Exception as e:
        print("Error:",e)
    execute_from_command_line(sys.argv)
