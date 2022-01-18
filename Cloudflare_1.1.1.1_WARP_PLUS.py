import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys


def waterMark():
    print("+--------------------------------------+")
    print("| Cloudflare | 1.1.1.1 WARP+           |")
    print("+------------+-------------------------+")
    print("|            | https://rvnrstnsyh.dev  |")
    print("|            | re@rvnrstnsyh.dev       |")
    print("+--------------------------------------+")
    return


os.system("title Cloudflare 1.1.1.1 WARP+ by rvnrstnsyh")
os.system('cls' if os.name == 'nt' else 'clear')
waterMark()
referrer = input("[#] Enter the WARP+ ID:")


def generateSTR(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitSTR(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitSTR(3)}/reg'


def execute():
    try:
        install_id = generateSTR(22)
        body = {"key": "{}=".format(generateSTR(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, generateSTR(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                        "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(error)


def countdown(seconds):
    for iteration in range(seconds):
        time.sleep(1)
        sys.stdout.write(
            f"\r[*] After {seconds - iteration} seconds, a new request will be sent.")


s_Gb = 0
f_Gb = 0
while True:
    result = execute()
    if result == 200:
        s_Gb = s_Gb + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        loading = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%",
                   "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
        waterMark()
        print(f"[-] Work on ID: {referrer}")
        for i in range(len(loading)):
            time.sleep(0.5)
            sys.stdout.write("\r[+] " + loading[i % len(loading)])
            sys.stdout.flush()
        print(f"\n[!] {s_Gb} GB has been successfully added to your account.")
        print(f"[#] Total: {s_Gb} success, {f_Gb} fail")
        countdown(20)
    else:
        b = b + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[:(] Error when connecting to server.")
        print(f"[#] Total: {s_Gb} success, {f_Gb} fail")
