import requests
import time
import netifaces

def get_ip_address(interface='wlan0'):
    try:
        addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if addresses:
            return addresses[0]['addr']
        else:
            return None
    except ValueError as e:
        print('Error',e)
        return None

if __name__ == "__main__":
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
                while response.status_code != 200
                print("Error:", response.status_code)
                time.sleep(1)
                response = requests.get('http://10.0.0.25/ip_configure',data=data)
        except Exception as e:
            print("Error:",e)
