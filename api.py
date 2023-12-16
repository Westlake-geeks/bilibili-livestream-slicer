import requests
import urllib
import json
import re
import time
import re
initial_uid = "9999"
live_api = "https://api.live.bilibili.com/room/v1/Room/room_init?id=%s" % initial_uid
stream_api = "https://api.live.bilibili.com/room/v1/Room/playUrl?cid=%s&quality=4&platform=web" % initial_uid


def my_request(url):
    headers = dict()
    headers['cookie'] = r"buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO2616596088417426; rpdid=|(k|m|))Y~k~0J'uYY)lmlul~; hit-new-style-dyn=1; go-back-dyn=1; is-2022-channel=1; header_theme_version=CLOSE; CURRENT_PID=b03f3c10-ceb5-11ed-b59d-47f8dacf4eec; FEED_LIVE_VERSION=V8; buvid3=103FCEA2-4D34-4196-5E7B-7321C8A1082118620infoc; b_nut=1690476718; _uuid=B1038F2AB-E8CD-29A2-4728-F82FE285F59D84428infoc; buvid4=CFCD8B8D-0FCC-F601-2753-DA825E11CFE613020-022072800-fr%2BgMSZdqRJTFAAYsS9ACQ%3D%3D; i-wanna-go-back=-1; b_ut=5; hit-dyn-v2=1; i-wanna-go-feeds=2; DedeUserID=325718681; DedeUserID__ckMd5=319313351948fd48; CURRENT_QUALITY=116; SESSDATA=c555e98c%2C1711883936%2Caf616%2Aa2CjAD_KFN4n_1-0P_VrGmaHuTOhode3kKsjtR7Aq0iz1U5TFRzKUl69JUDZ-5W532pswSVkFKMUpyQkQ3NmlWYldjLWtnSG9hcG9lQ1RYa0VKaEh3TFlybGxjdlpJQkkwekYwYy0tckZhc1d3eWlrT1k2NHpvQmQtS1MtUGlxU2RxdEM2UFcyWWlnIIEC; bili_jct=f30d6a38050b9fd22f87748b88e5c40f; sid=8nj7ny5x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY2MDgwNDYsImlhdCI6MTY5NjM0ODc4NiwicGx0IjotMX0.P976bqS0e1zm2k4khjnX5aqxWCmSIE-zA6MlVXq32wo; bili_ticket_expires=1696607986; fingerprint=c2d58d86c60e35d56558bf9942a9deac; CURRENT_FNVAL=4048; home_feed_column=5; browser_resolution=1699-945; share_source_origin=WEIXIN; bsource=share_source_weixinchat; bp_video_offset_325718681=849021837940621320; buvid_fp=c2d58d86c60e35d56558bf9942a9deac; b_lsid=5469973A_18B009161BC; PVID=1"
    headers['Accept-Encoding'] = 'identity'
    headers['referer'] = 'https://www.bilibili.com/video/BV1XF411C7xh/?spm_id_from=333.1007.tianma.1-3-3.click&vd_source=d4827c2f1802c9c5b667bc324c406c18'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'

    response = requests.get(url=url, headers=headers)
    return response.text


def is_live(uid):
    live_api = "https://api.live.bilibili.com/room/v1/Room/room_init?id=%s" % str(
        uid)
    rtn = my_request(live_api)
    data_dict = json.loads(rtn)

    data_value = data_dict.get('data')
    live_status_value = data_value.get('live_status')
    if live_status_value:
        return True
    else:
        return False


def get_stream_url(uid):
    stream_api = "https://api.live.bilibili.com/room/v1/Room/playUrl?cid=%s&quality=4&platform=web" % uid

    rtn = my_request(stream_api)
    data_dict = json.loads(rtn)

    data_value = data_dict.get('data')
    durl_value = data_value.get('durl')

    headers = dict()
    headers['cookie'] = r"buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO2616596088417426; rpdid=|(k|m|))Y~k~0J'uYY)lmlul~; hit-new-style-dyn=1; go-back-dyn=1; is-2022-channel=1; header_theme_version=CLOSE; CURRENT_PID=b03f3c10-ceb5-11ed-b59d-47f8dacf4eec; FEED_LIVE_VERSION=V8; buvid3=103FCEA2-4D34-4196-5E7B-7321C8A1082118620infoc; b_nut=1690476718; _uuid=B1038F2AB-E8CD-29A2-4728-F82FE285F59D84428infoc; buvid4=CFCD8B8D-0FCC-F601-2753-DA825E11CFE613020-022072800-fr%2BgMSZdqRJTFAAYsS9ACQ%3D%3D; i-wanna-go-back=-1; b_ut=5; hit-dyn-v2=1; i-wanna-go-feeds=2; DedeUserID=325718681; DedeUserID__ckMd5=319313351948fd48; CURRENT_QUALITY=116; SESSDATA=c555e98c%2C1711883936%2Caf616%2Aa2CjAD_KFN4n_1-0P_VrGmaHuTOhode3kKsjtR7Aq0iz1U5TFRzKUl69JUDZ-5W532pswSVkFKMUpyQkQ3NmlWYldjLWtnSG9hcG9lQ1RYa0VKaEh3TFlybGxjdlpJQkkwekYwYy0tckZhc1d3eWlrT1k2NHpvQmQtS1MtUGlxU2RxdEM2UFcyWWlnIIEC; bili_jct=f30d6a38050b9fd22f87748b88e5c40f; sid=8nj7ny5x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY2MDgwNDYsImlhdCI6MTY5NjM0ODc4NiwicGx0IjotMX0.P976bqS0e1zm2k4khjnX5aqxWCmSIE-zA6MlVXq32wo; bili_ticket_expires=1696607986; fingerprint=c2d58d86c60e35d56558bf9942a9deac; CURRENT_FNVAL=4048; home_feed_column=5; browser_resolution=1699-945; share_source_origin=WEIXIN; bsource=share_source_weixinchat; bp_video_offset_325718681=849021837940621320; buvid_fp=c2d58d86c60e35d56558bf9942a9deac; b_lsid=5469973A_18B009161BC; PVID=1"
    headers['Accept-Encoding'] = 'identity'
    headers['referer'] = 'https://www.bilibili.com/video/BV1XF411C7xh/?spm_id_from=333.1007.tianma.1-3-3.click&vd_source=d4827c2f1802c9c5b667bc324c406c18'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'

    retry_time = 0
    return durl_value, headers
    if durl_value:
        try:
            return durl_value, headers
        except Exception as e:
            time.sleep(1)
            print("retry", retry_time,
                  "]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print(e)
            retry_time += 1
            pass


def get_name(uid):
    live_api = "https://api.live.bilibili.com/room/v1/Room/room_init?id=%s" % str(
        uid)
    rtn = my_request(live_api)
    data_dict = json.loads(rtn)

    data_value = data_dict.get('data')
    duid_value = data_value.get('uid')

    home_url = "https://space.bilibili.com/%s/" % duid_value

    headers = {
        'cookie': "buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO2616596088417426; rpdid=|(k|m|))Y~k~0J'uYY)lmlul~; hit-new-style-dyn=1; go-back-dyn=1; is-2022-channel=1; header_theme_version=CLOSE; CURRENT_PID=b03f3c10-ceb5-11ed-b59d-47f8dacf4eec; FEED_LIVE_VERSION=V8; buvid3=103FCEA2-4D34-4196-5E7B-7321C8A1082118620infoc; b_nut=1690476718; _uuid=B1038F2AB-E8CD-29A2-4728-F82FE285F59D84428infoc; buvid4=CFCD8B8D-0FCC-F601-2753-DA825E11CFE613020-022072800-fr%2BgMSZdqRJTFAAYsS9ACQ%3D%3D; i-wanna-go-back=-1; b_ut=5; hit-dyn-v2=1; i-wanna-go-feeds=2; DedeUserID=325718681; DedeUserID__ckMd5=319313351948fd48; CURRENT_QUALITY=116; SESSDATA=c555e98c%2C1711883936%2Caf616%2Aa2CjAD_KFN4n_1-0P_VrGmaHuTOhode3kKsjtR7Aq0iz1U5TFRzKUl69JUDZ-5W532pswSVkFKMUpyQkQ3NmlWYldjLWtnSG9hcG9lQ1RYa0VKaEh3TFlybGxjdlpJQkkwekYwYy0tckZhc1d3eWlrT1k2NHpvQmQtS1MtUGlxU2RxdEM2UFcyWWlnIIEC; bili_jct=f30d6a38050b9fd22f87748b88e5c40f; sid=8nj7ny5x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY2MDgwNDYsImlhdCI6MTY5NjM0ODc4NiwicGx0IjotMX0.P976bqS0e1zm2k4khjnX5aqxWCmSIE-zA6MlVXq32wo; bili_ticket_expires=1696607986; fingerprint=c2d58d86c60e35d56558bf9942a9deac; CURRENT_FNVAL=4048; home_feed_column=5; browser_resolution=1699-945; share_source_origin=WEIXIN; bsource=share_source_weixinchat; bp_video_offset_325718681=849021837940621320; buvid_fp=c2d58d86c60e35d56558bf9942a9deac; b_lsid=5469973A_18B009161BC; PVID=1",
        # 'referer': "https://space.bilibili.com/353609978/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }
    response = requests.get(url=home_url, headers=headers)
    user_name = re.findall(r'<title>(.*?)的个人空间', response.text)[0]
    if user_name:
        return (user_name)
    else:
        return ("未找到指定用户名称")


# print(get_stream_url(7734200))
