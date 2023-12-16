import os
import json
from api import is_live, get_stream_url, get_name, my_request

import traceback
import sys
import re
import streamlink
import threading
import requests

import time
import datetime
from urllib import request
import urllib
import socket
socket.setdefaulttimeout(5.0)


def record(real_url, file_name, headers):
    if not real_url:
        return
    res = None

    try:
        with urllib.request.urlopen(urllib.request.Request(real_url, headers=headers)) as response:
            size = 0

            with open(file_name, 'wb') as f:
                print('starting download from:\n%s\nto:\n%s' %
                      (real_url, file_name))
                chunk_size = 64*1024

                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        print('连接中断')
                        break

                    f.write(chunk)
                    #size += len(chunk)
                    #print('{:<4.2f} MB downloaded'.format(
                    #    size/1024/1024), datetime.datetime.now(), end="\r")
    except Exception as e:
        print("=============================")
        print(e)
        print("=============================")
    finally:
        print("finnally")
        if res:
            res.close()
            print("res.close()")

        if os.path.isfile(file_name) and os.path.getsize(file_name) == 0:
            os.remove(file_name)
            print("os.remove(file_name)")

def __main__(id,filename):
    #conf = json.load(open("_config.json"))
    _id = id
    _name = get_name(int(_id))
    _path = "videos/"

    if not os.path.exists(_path):
        raise "path not exists"


    while 1:
        try:
            live_status = is_live(int(_id))
            print('live_status:', live_status)
        except Exception as e:
            print(e)
            continue

        if live_status == False:

            print("[%s]未开播" % _id, datetime.datetime.now(), end="\r")
            time.sleep(5)
            pass
        else:
            # send_wechat_notification(_name+' '+'标题占位', '直播链接占位00000')
            try:
                stream_url, headers = get_stream_url(_id)
                url_dict = stream_url[0]
                real_url = url_dict['url']
                if real_url == None:
                    print("开播了但是没有源")
                    continue

                record(real_url, filename, headers)
            except:
                pass
        time.sleep(1)
