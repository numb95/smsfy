#!/usr/bin/env python3
import json

import requests

from kavenegar import *


def get_data():
    """ what does this function do?"""
    with open('smsfy.json') as fp:
        json_data = json.load(fp)

        uptime_API_KEY = json_data['uptime']['api_key']
        uptime_URL = json_data['uptime']['url']
        kavenegar_API_KEY = json_data['kavenegar']['api_key']
        kavenegar_receptor = json_data['kavenegar']['receptor']
        return uptime_API_KEY, uptime_URL, kavenegar_API_KEY, kavenegar_receptor
    return None

def uptime(uptime_API_KEY, uptime_URL):
    """ what does this function do?"""
    payload = {'api_key': uptime_API_KEY}

    with requests.post(uptime_URL, data = payload) as response:
        response_status = response.json()['monitors'][0]['status']

    if response_status == 9:
        return False
    if response_status == 2:
        return True
    else:
        return 0

def sms (stat, kavenegar_API_KEY, kavenegar_receptor):
    """ what does this function do?"""
    api = KavenegarAPI(kavenegar_API_KEY)
    parameteres ={'receptor': kavenegar_receptor,'message': 'server is DOWN'}

    if not stat:
        response = api.sms_send(parameteres)

def main():
    #for uptime_item in uptime_API_KEY:
    uptime_API_KEY, uptime_URL, kavenegar_API_KEY, kavenegar_Receptor = get_data()
    print (get_data())       
    sms(uptime(uptime_API_KEY, uptime_URL),kavenegar_API_KEY, kavenegar_receptor)

if __name__ == '__main__':
    main()
