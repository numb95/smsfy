import requests 
from kavenegar import *
import json
# Todo()
# 0) temporary run api keys and reciever from a dotfile
# 1) make it systemd friendly, which can run on background 
# 2) make a config file with yaml or json format which can specified the API Keys and reciever and 
# 3) handling custom message types
# 4) make it to run config file in /etc/smsify.conf as a default location
# 5) using -c /home/user/smsfy.conf as a custom located config
# 4) change the code to run and import config files with multiply reciever 
# 5) make a init argument which can create config file in default or user specified locatio,
# 6) create systemd file and enable / start it in init command
# 7) add multiply reciever wizard in init
# 8) add multiply hosts with uptime robot nickname in it
def get_data():
    file = open('smsify.conf')
    json_data = json.load(file)
    uptime_API_KEY = json_data['uptime']['api_key']
    uptime_URL = json_data['uptime']['url']
    kavenegar_API_KEY = json_data['kavenegar']['api_key']
    kavenegar_Receptor = json_data['kavenegar']['receptor']
    return uptime_API_KEY, uptime_URL, kavenegar_API_KEY, kavenegar_Receptor
#for uptime_item in uptime_API_KEY:
uptime_API_KEY, uptime_URL, kavenegar_API_KEY, kavenegar_Receptor = get_data()
print (get_data())       
def uptime(uptime_API_KEY, uptime_URL):
    API_KEY = uptime_API_KEY
    API_URL = uptime_URL
    payload = {'api_key': API_KEY}
    response = requests.post(API_URL, data = payload)
    response_status = response.json()['monitors'][0]['status']
    if response_status == 9:
        return False
    if response_status == 2:
        return True
    else:
        return 0
def sms (stat, kavenegar_API_KEY, kavenegar_Receptor):
    api = KavenegarAPI(kavenegar_API_KEY)
    parameteres ={'receptor': kavenegar_Receptor,'message': 'server is DOWN'}
    if not stat:
        response = api.sms_send(parameteres)
sms(uptime(uptime_API_KEY, uptime_URL),kavenegar_API_KEY, kavenegar_Receptor)

