import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow
from bilibili_api import live, sync, Credential,video_uploader
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from api import is_live
from matplotlib.backends.backend_pdf import PdfPages
import main 
from moviepy.editor import VideoFileClip
import os
import time
import json
import sys
import moviepy
import whisper
from selenium import webdriver
import requests
from api import get_name
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
#from chaojiying import Chaojiying_Client
#裁剪模块
from PIL import Image
#去除识别


v2t_model = whisper.load_model('medium')
from PIL import Image, ImageDraw, ImageFont

def add_text_with_outline(image_path, text, font_size, position, text_color, outline_color, outline_width, output_path):
    # 打开图像
    image = Image.open(image_path).convert("RGBA")
    
    # 调整图像大小
    image = image.resize((960, 600))
    
    # 创建一个与图像大小相同的画布
    drawing = ImageDraw.Draw(image)
    
    # 加载字体
    font = ImageFont.truetype("C:/Windows/Fonts/STZHONGS.ttf", font_size)
    font_size = 100
    
    # 计算文本尺寸
    text_width, text_height = drawing.textbbox((0, 0, image.width, image.height), text, font=font)[:2]
    
    # 计算文本位置
    image_width, image_height = image.size
    position_x = (image_width - text_width) // 2-400
    position_y = (image_height - text_height) // 2
    
    # 分两行显示文本
    if len(text) > 10:
        text_line1 = text[:len(text)//2]
        text_line2 = text[len(text)//2:]
        
        # 计算第一行文本的位置
        text_width1, _ = drawing.textbbox((0, 0, image.width, image.height), text_line1, font=font)[:2]
        position1 = (position_x, position_y - text_height-100)
        
        # 计算第二行文本的位置
        text_width2, _ = drawing.textbbox((0, 0, image.width, image.height), text_line2, font=font)[:2]
        position2 = (position_x, position_y)
        
        # 计算描边的位置
        outline_position1 = (position1[0] - outline_width, position1[1] - outline_width)
        outline_position2 = (position2[0] - outline_width, position2[1] - outline_width)
        
        # 绘制描边文本
        drawing.text(outline_position1, text_line1, font=font, fill=outline_color)
        drawing.text(outline_position2, text_line2, font=font, fill=outline_color)
        
        # 绘制文本
        drawing.text(position1, text_line1, font=font, fill=text_color)
        drawing.text(position2, text_line2, font=font, fill=text_color)
    else:
        position = (position_x, position_y)
        outline_position = (position[0] - outline_width, position[1] - outline_width)
        
        # 绘制描边文本
        drawing.text(outline_position, text, font=font, fill=outline_color)
        drawing.text(position, text, font=font, fill=text_color)
    
    # 保存图像
    image.save(output_path)
    #image.show()

import re 
def get_live_title(uid):
    live_url = "https://live.bilibili.com/%s?live_from=84002&spm_id_from=333.337.0.0" % uid
    headers = {
        'cookie': "buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO2616596088417426; rpdid=|(k|m|))Y~k~0J'uYY)lmlul~; hit-new-style-dyn=1; go-back-dyn=1; is-2022-channel=1; header_theme_version=CLOSE; CURRENT_PID=b03f3c10-ceb5-11ed-b59d-47f8dacf4eec; FEED_LIVE_VERSION=V8; buvid3=103FCEA2-4D34-4196-5E7B-7321C8A1082118620infoc; b_nut=1690476718; _uuid=B1038F2AB-E8CD-29A2-4728-F82FE285F59D84428infoc; buvid4=CFCD8B8D-0FCC-F601-2753-DA825E11CFE613020-022072800-fr%2BgMSZdqRJTFAAYsS9ACQ%3D%3D; i-wanna-go-back=-1; b_ut=5; hit-dyn-v2=1; i-wanna-go-feeds=2; DedeUserID=325718681; DedeUserID__ckMd5=319313351948fd48; CURRENT_QUALITY=116; SESSDATA=c555e98c%2C1711883936%2Caf616%2Aa2CjAD_KFN4n_1-0P_VrGmaHuTOhode3kKsjtR7Aq0iz1U5TFRzKUl69JUDZ-5W532pswSVkFKMUpyQkQ3NmlWYldjLWtnSG9hcG9lQ1RYa0VKaEh3TFlybGxjdlpJQkkwekYwYy0tckZhc1d3eWlrT1k2NHpvQmQtS1MtUGlxU2RxdEM2UFcyWWlnIIEC; bili_jct=f30d6a38050b9fd22f87748b88e5c40f; sid=8nj7ny5x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY2MDgwNDYsImlhdCI6MTY5NjM0ODc4NiwicGx0IjotMX0.P976bqS0e1zm2k4khjnX5aqxWCmSIE-zA6MlVXq32wo; bili_ticket_expires=1696607986; fingerprint=c2d58d86c60e35d56558bf9942a9deac; CURRENT_FNVAL=4048; home_feed_column=5; browser_resolution=1699-945; share_source_origin=WEIXIN; bsource=share_source_weixinchat; bp_video_offset_325718681=849021837940621320; buvid_fp=c2d58d86c60e35d56558bf9942a9deac; b_lsid=5469973A_18B009161BC; PVID=1",
        # 'referer': "https://space.bilibili.com/353609978/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }
    response = requests.get(url=live_url, headers=headers)
    live_title = re.findall(r'<title id="link-app-title">(.*?) - ', response.text)[0]
    if live_title:
        return (live_title)
    else:
        return ("未找到指定直播间名称")
def clipP(file_name_in , id ,start_time, end_time ):

    #file_name_in = r"C:\Users\s1ctx\Desktop\小组作业\bilibili\videos\HiiroVTuber_2023_12_10_05_23_34_650471__.flv"
    #base_filename = os.path.basename(file_name_in)
    # Provide the correct file path to the video file
    
    output_path = r'C:\Users\s1ctx\Desktop\groupwork\videos'
    output_filename = f'Cliped_{id}_{start_time}-{end_time}.mp4'
    output_file_path = os.path.join(output_path, output_filename)

    os.system(f'ffmpeg -i {file_name_in} -ss {start_time} -t {end_time-start_time} -c:v libx264 -c:a copy {output_file_path}')
    #ffmpeg -i Cliped_21452505_3289-3321.mp4 -ss 00:00:01 -vframes 1 output.jpg
    os.system(f'ffmpeg -i {output_file_path} -ss 00:00:01 -vframes 1 {output_file_path}.png')

    
    return output_file_path

    ##video_clip = video_in.subclip(start_time, end_time)
    ## 构造输出文件的路径
    ##output_path = r'C:\Users\s1ctx\Desktop\小组作业\videos'
    ##output_filename = f'Cliped_{id}_{start_time}-{end_time}.mp4'


    ##output_file_path = os.path.join(output_path, output_filename)
    ##video_clip.write_videofile(output_file_path, codec='libx264')

que = {}
flag = False

async def uploader_video(output_file_path,id):
    try:
        result = v2t_model.transcribe(output_file_path,language= 'Chinese')
        words = result['text']
    except:
        words = '略'
    up_name = get_name(int(id))
    room_name = get_live_title(int(id))
    try:
        url = "https://openkey.cloud/v1/chat/completions"
        headers = {
        'Content-Type': 'application/json',
        # 填写OpenKEY生成的令牌/KEY，注意前面的 Bearer 要保留，并且和 KEY 中间有一个空格。
        'Authorization': 'Bearer sk-8g5sXADrhra9gSfcu9KD90IW8gRQJ7lRxxfKvGV5aMwk62rV'
        }

        data = {
        "model": "gpt-3.5-turbo-1106",
        "messages": [{"role": "user", "content": f"这里给出博主 {up_name} 的名为 {room_name} 的直播切片的文字内容，请总结并取一个合适的‘诙谐、风趣’的标题（仅仅输出标题）：\n {words} "}]
        }
        response = requests.post(url, headers=headers, json=data)
        title = (response.json()['choices'][0]['message']['content'])
        #封面
        
    except:
        title = f"{up_name} 的 {room_name} 的 {str(datetime.now())}"
        print('错误，没有连接到GPT')

    image_path = output_file_path+'.png'
    output_path = output_file_path+'.png'

    text = title
    font_size = 100
    position = (100, 100)
    text_color = (255, 255, 0)  # 白色
    outline_color = (0, 0, 0)  # 黄色
    outline_width = 2
    try :
        add_text_with_outline(image_path, text, font_size, position, text_color, outline_color, outline_width, output_path)
    except:
        pass
    print(title)
    print('----------------------------------------正在上传---------------------------------------------')
    credential = Credential(
            sessdata="",
            bili_jct="",
            buvid3="",
            dedeuserid=""
        )
    # 具体请查阅相关文档
    meta = {
        "act_reserve_create": 0,
        "copyright": 1,
        "source": "",
        "desc": "",
        "desc_format_id": 0, 
        "dynamic": "",
        "interactive": 0,
        "no_reprint": 1,
        "open_elec": 0,
        "origin_state": 0,
        "subtitles": {
            "lan": "",
            "open": 0
        },
        "tag": f"直播切片,{up_name},{room_name},搞笑",
        "tid": 138 ,
        "title": title,
        "up_close_danmaku": False,
        "up_close_reply": False,
        "up_selection_reply": False,
        "dtime": 0
    }
    page = video_uploader.VideoUploaderPage(path = output_file_path,title=title,description='')
    uploader = video_uploader.VideoUploader([page], meta, credential)#, cover = 'cover.png')
    try: 
        @uploader.on("__ALL__")
        async def ev(data):
            print(data)
        await uploader.start()
    except:
        print('上传失败')
        print(output_file_path)
        print(title)
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("detach",True)
        web  = webdriver.Chrome()
        web.get('http://www.bilibili.com')
        f = open('cookie.txt','r')
        listcookie = json.loads(f.read())#读取文件中的cookies数据

        for cookie in listcookie:
            web.add_cookie(cookie)#将cookies数据添加到浏览器

        time.sleep(3)

        web.get("https://member.bilibili.com/platform/upload/video/frame")
        # 等待加载

        time.sleep(3)
        path_mp4 =output_file_path
        upload_button = web.find_element(By.XPATH, "//input[@type='file']")
        upload_button.send_keys(path_mp4)
        time.sleep(2)
        try:
            buttum = web.find_element(By.XPATH, '//*[@id="video-up-app"]/div[3]/div/div[3]/button')
            buttum.click()
            time.sleep(0.5)
            buttum = web.find_element(By.XPATH, '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div/div/div[1]/div[1]/div/div')
            buttum.click()
        except:
            pass
        try:
            time.sleep(1.5)
            upload_cover= web.find_element(By.XPATH,'//*[@id="video-up-app"]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/input')
            upload_cover.send_keys(path_mp4+'.png')
            time.sleep(0.5)
            buttum = web.find_element(By.XPATH,'//*[@id="video-up-app"]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div[1]/div/div[3]/div/div/button[2]')
            buttum.click()
            time.sleep(0.5)
            title_input = web.find_element(By.XPATH,'//*[@id="video-up-app"]/div[2]/div/div/div[1]/div[2]/div[3]/div/div[2]/div/input')
            title_input.send_keys(Keys.CONTROL, 'a')
            title_input.send_keys(title+f'【{up_name}】')
            time.sleep(1)
            tags=web.find_elements(By.CLASS_NAME,"hot-tag-item")
        except:
            pass
        try:
            for index, tag in enumerate(tags):
                if index < 5:
                    # 点击元素
                    tag.click()
        except:
            pass
        try:
            time.sleep(1)
            submit_button = web.find_element(By.CLASS_NAME, "submit-add")
            submit_button.click()
            time.sleep(100000)
        except:
            pass



#建一个用于爬取直播视频的线程，核心代码是main.__main__(id)，其中id是房间号是一个str
class ThreadC_C(QtCore.QThread):
    # 多线程
    def __init__(self, file_name,num,start_time,end_time):
        super(ThreadC_C, self).__init__()
        self.num = num
        self.start_time = start_time
        self.end_time = end_time
        #self.now = datetime.now()
        self.file_name = file_name
    def run(self):
        #print('1111111111111111111111-------------------------------------------------------------------------------------111111111111111111111111-------------------------------------111')
        time.sleep(10)#wait for 10 seconds
        output_file_path = clipP(self.file_name,self.num,self.start_time,self.end_time)
        try: 
            sync(uploader_video(output_file_path,self.num))
        except:
            print('上传失败')
        

class ThreadV(QtCore.QThread):
    # 多线程
    def __init__(self, num):
        super(ThreadV, self).__init__()
        self.num = num
        self.now = datetime.now()+ timedelta(seconds=2)
        self.file_name = "videos/" + str(self.num) + self.now.strftime("_%Y_%m_%d_%H_%M_%S_%f_"+"_.flv")
        self.clip = 0
    def run(self):
        #pass
        main.__main__(self.num,self.file_name)

class Thread(QtCore.QThread):
    # 多线程
    def __init__(self, num):
        super(Thread, self).__init__()
        self.num = num
        

    def run(self): #爬取弹幕
        def parse_datetime(datetime_str):
            return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        
        
        credential = Credential(
            sessdata="daaa877d%2C1718024867%2C467ef%2Ac1CjBp5PW0dsSQNj39aOl6oD7y3C6KnP_5VRmTVGJBAI822wuSR5E-aQqFHqOr9C8qKoISVldObldPTmgwM0lFV3pOWWlDeGlyLTI5UWtjRmQ2T1NScGFyQzNHRnczeGRtUnI2S0xPNXV2TVM1N0NHS3ZSc1A4RXBweVphcURsTExiano1SXl6aDVRIIEC",
            bili_jct="71b585f44771a21249f38244524e8a65",
            buvid3="E69A492D-3A10-E4EE-138B-ED2AE0BC42CE15929infoc",
            dedeuserid="142351113"
        )


        room = live.LiveDanmaku(self.num, credential=credential)
        danmu_count = {}

        danmu_sentiment = {}
        sentiment_list = []
        #main.__main__(self.num)
        danmu_list={}

        @room.on('DANMU_MSG')
        async def on_danmaku(event):
            # 收到弹幕f
            timestamp = event["data"]["info"][9]['ts']
            dt_object = datetime.fromtimestamp(timestamp)
            danmu = event["data"]["info"][1]
            #print(danmu)
            ren = event["data"]["info"][2][1]
            time = str(dt_object)
            global que
            try:
                datetime_obj = parse_datetime(time)
                # 5s
                time_key = datetime_obj - timedelta(seconds=datetime_obj.second % 5)
                #40 s
                #time_key = datetime_obj - timedelta(seconds=datetime_obj.second % 40)            
                #time_key = datetime_obj - timedelta(seconds=0)
                #danmu_count[time_key] = danmu_count.get(time_key, 0) + 1
                #time_key = datetime_obj - timedelta(seconds=1)
                #danmu_count[time_key] = danmu_count.get(time_key, 0) + 1
                #time_key = datetime_obj - timedelta(seconds=2)
                #danmu_count[time_key] = danmu_count.get(time_key, 0) + 1
                #time_key = datetime_obj - timedelta(seconds=3)
                #danmu_count[time_key] = danmu_count.get(time_key, 0) + 1
                #time_key = datetime_obj - timedelta(seconds=4)
                que[self.num][time_key] = que[self.num].get(time_key, 0) + 1
            except:
                print("Someting Wrong!")
                
        sync(room.connect())

class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    # 继承UI窗口类Ui_MainWindow
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.roomlist = [] # 直播间列表
        self.processlist = []
        self.roomstatus = {} # 开播状态
        self.roomtot = 0
        self.maximum = 40 # 多线程上限
        self.addButton.clicked.connect(self.add) # 把UI上的按钮连接到控制函数
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
    
    def add(self): # 添加新链接
        self.roominput = self.roomEdit.text()
        if not self.roominput.isdigit():
            # self.logPoster.append('invalid room number!')
            print('invalid room number!')
            pass
        elif self.roomtot < self.maximum:
            try:
                self.status = is_live(int(self.roominput))
                self.roomtot += 1
                self.roomlist.append(self.roominput)
                self.roomstatus[self.roomlist[-1]] = self.status
                if self.roomstatus[self.roomlist[-1]]:
                    self.logPoster.addItem(self.roomlist[-1] + '(online)')
                else:
                    self.logPoster.addItem(self.roomlist[-1] + '(offline)')
            except:
                print("room inexist")
            
            # self.logPoster.append('room ' + self.roomlist[-1] + ' added.')
            # self.roomlist = list(set(self.roomlist))
            # print(self.roomlist)
        else:
            # self.logPoster.append('too more rooms!')
            print('too more rooms!')

    def initroom(self, num): # 初始化直播间进程
            que[int(num)] = {}
            self.processlist.append(Thread(int(num)))
            self.processlist[-1].start()
            self.processlist.append(ThreadV(int(num)))
            try:
                self.processlist[-1].start()
            except:
                print("Someting Wrong!")
    
    def start(self): # 开始多线程爬取
        global que, flag
        que = {}
        flag = True
        mean = []
        cut_now = []
        plt.ion()  # 打开交互模式
        fig, ax = plt.subplots()
        line = [ax.plot([], [], label = get_name(self.roomlist[i]))[0] for i in range(self.roomtot)]
        tail = [0] * self.roomtot
        last = []
        for i in range(len(self.roomlist)): 
            mean.append(0)
            cut_now.append(0)
            last.append(0)
            if self.roomstatus[self.roomlist[i]]:
                self.initroom(self.roomlist[i])
                self.logPoster.takeItem(i)
                self.logPoster.insertItem(i, self.roomlist[i] + '(processing)')
                # itemnow = self.logPoster.item(self.roomlist.index(i))
        
        
        while flag:
            
            for i in range(self.roomtot):
                if self.roomstatus[self.roomlist[i]]:
                    if tail[i] > 12 * 2: # lager than 1 min 
                        if max(list(que[int(self.roomlist[i])].values())[-1] , list(que[int(self.roomlist[i])].values())[-2]) > min(max(2*mean[i],12),85) :
                            
                            if last[i] != 0: # 前一段已经结束但是没有 切

                                if datetime.now() < last[i] + timedelta(seconds=10):
                                    last[i]=datetime.now()
                                    last[i]=0
                                    pass #两段的间隔时间太短无事情发生
                                else :
                                    #结算切片
                                    self.logPoster.addItem('clip at room'+ self.roomlist[i] +' : start at' + str(cut_now[i]) + ',end at'+ str(last[i]))
                                    whz = ThreadC_C(self.processlist[2*i+1].file_name,self.processlist[2*i+1].num,(cut_now[i]-self.processlist[2*i+1].now-timedelta(seconds=17)).seconds,(last[i] - self.processlist[2*i+1].now).seconds )
                                    whz.start()
                                    cut_now[i] = 0
                                    last[i] = 0

                                
                            if cut_now[i] == 0  :
                                This_time = list(que[int(self.roomlist[i])].keys())[-1] 
                                cut_now[i] = This_time
                        
                        else:
                            if list(que[int(self.roomlist[i])].values())[-1] < 2*mean[i] and list(que[int(self.roomlist[i])].values())[-3] < 2*mean[i] and list(que[int(self.roomlist[i])].values())[-2]  < 2*mean[i]:  
                                #记录结束时间点
                                if cut_now[i] != 0  and  last[i] ==0:
                                    This_time = datetime.now()
                                    last[i] = This_time
                                    #self.logPoster.append('clip at room'+ self.roomlist[i] +' : start at' + str(cut_now[i]) + ',end at'+ str(This_time + timedelta(seconds=10)))
                                    #whz = ThreadC_C(self.processlist[2*i-1].file_name,self.processlist[2*i-1].num,())
                                    #self.logPoster.append('clip at room'+ self.roomlist[i] +' : start at' + str(cut_now[i]) + ',end at ' + str(This_time + timedelta(seconds=10)))
                                    #whz = ThreadC_C(self.processlist[2*i-1].file_name,self.processlist[2*i-1].num,(cut_now[i]-self.processlist[2*i-1].now-timedelta(seconds=6)).seconds,(This_time - self.processlist[2*i-1].now).seconds )
                                    #whz.start()
                                if last[i] != 0: # 前一段已经结束但是没有 切
                                    if datetime.now() > last[i] + timedelta(seconds=10):
                                        #结算切片
                                        self.logPoster.addItem('clip at room'+ self.roomlist[i] +' : start at' + str(cut_now[i]) + ',end at'+ str(last[i]))
                                        whz = ThreadC_C(self.processlist[2*i+1].file_name,self.processlist[2*i+1].num,(cut_now[i]-self.processlist[2*i+1].now-timedelta(seconds=15)).seconds,(last[i] - self.processlist[2*i+1].now).seconds )
                                        whz.start()
                                        cut_now[i] = 0
                                        last[i] = 0


                    if len(que[int(self.roomlist[i])]) > tail[i]:
                        tail[i] = len(que[int(self.roomlist[i])])
                        x = list(que[int(self.roomlist[i])].keys())
                        y = list(que[int(self.roomlist[i])].values())
                        line[i].set_data(x,y)
                        mean[i]= sum(y)/len(y)                        
                        #print('----------')
                        #print(que[int(self.roomlist[i])])
                        #print('----------')
                        #print(que[int(self.roomlist[i])][tail[i]][1][0])
                        #if que[int(self.roomlist[i])][tail[i]][1][0] > 30:
                        #    print('------------------------切片------------------------')
                        # 调整坐标轴范围
                        ax.relim()
                        ax.autoscale_view()
                        # 刷新图形
                        plt.draw()
                        plt.pause(0.03)
                else:
                    self.roomstatus[self.roomlist[i]] =is_live(self.roomlist[i])
                    print(self.roomlist[i] + ' is '+ str(self.roomstatus[self.roomlist[i]]))
                    if self.roomstatus[self.roomlist[i]]:
                        self.logPoster.insertItem(i, self.roomlist[i] + '(online)')
                        self.initroom(self.roomlist[i])
                        

            time.sleep(1)
    
    def stop(self): # 停止爬取
        global flag
        flag = False
        for i in self.processlist:
            i.terminate()
        for i in range(len(self.roomlist)):
            if self.roomstatus[self.roomlist[i]]:
                self.logPoster.takeItem(i)
                self.logPoster.insertItem(i, self.roomlist[i] + '(online)')
        # self.roomlist.clear()
        # self.roomtot = 0
        # self.processlist.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #获取控制台交互
    win = MainForm() #创建窗口
    win.show() #显示窗口
    sys.exit(app.exec_()) #退出控制台交互
