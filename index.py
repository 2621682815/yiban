####代码仅供学习参考，
####by 月初
import requests
import time
from datetime import datetime
import hashlib
import urllib3
#-------------------------------------------------------变量信息----------------------------------------------------------------#

zhh={
    1:"202153",###第一个账号
}
mmm={
    1: "密码",###第一个账号密码
}
n=0+1
zs = len(zhh)
while n<zs+1:
    zh = zhh[n]
    deomo_val = mmm[n]
    # ---------------------------------------------------------加密--------------------------------------------------------------#
    dt01 = datetime.today()
    xzrq = (dt01.date())
    t = time.time()
    rq = (str(int(t)))
    md5_val = hashlib.md5(deomo_val.encode('utf8')).hexdigest()
    j = (md5_val[:30])
    k = (md5_val[:5])
    m = (j[9:])
    l = (j[5:9])
    kk = k + "a" + l + "b" + m
    n=n+1
    # -------------------------------------------------登录提取cookie--------------------------------------------------------------#
    headersq = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Host': 'xggl.hnqczy.com',
        'Connection': 'keep-alive',
        'Content-Length': '57',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://xggl.hnqczy.com',
        'Referer': 'http://xggl.hnqczy.com/index;jsessionid=E4C1D2DFA72761FF80084C3175023A8D',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    urlq = "http://xggl.hnqczy.com/website/login"
    dataq = [
        ("uname", zh),
        ("pd_mm", kk)
    ]
    def post():
        r = requests.post(urlq, data=dataq, headers=headersq).headers['Set-Cookie']
        print(r)
        return r
    cooick = (post()[:43])
    cooick1 = (cooick[11:])
    # ---------------- ---------------------------------获取上次打卡记录josn--------------------------------------------------------------#
def get_xxx():
    url="http://xggl.hnqczy.com/content/student/temp/zzdk/lastone?_t_s_=1661221850154"
    headers = {'Host': 'xggl.hnqczy.com',
               'Connection': 'keep-alive',
               'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36;webank/h5face;webank/1.0 yiban_android/5.0.12',
               'X-Requested-With': 'XMLHttpRequest',
               'Referer': 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_=1661221849267',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               }
    cookies = {
        'JSESSIONID':cooick1,
    }
    rsp =requests.get(url, headers,cookies=cookies).json()
    return rsp
dkdz=get_xxx()['dkdz']
dkd=get_xxx()['dkd']
jzdDz2=get_xxx()['jzdDz2']
lxdh = get_xxx()["lxdh"]
print(get_xxx())
# ----------------------------------------------------------校验加密--------------------------------------------------------------#
def jm():
    http = urllib3.PoolManager()
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Cookie':'JSESSIONID='+cooick1}
    resp = http.request('GET', 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_=1661742092205',
                        headers=headers, )
    sj = (resp.data.decode())
    zzdk_token = (sj[sj.index('zzdk_token" value=\"') + 19:])
    zzdk_token = (zzdk_token[:zzdk_token.index('"/>')])
    return str(zzdk_token)
print(jm())
# ----------------------------------------------------------打卡--------------------------------------------------------------#
def post_xxx():
    url="http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_=1661311939332"
    headers = {'Host': 'xggl.hnqczy.com',
               'Connection': 'keep-alive',
               'Accept': '*/*',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36;webank/h5face;webank/1.0 yiban_android/5.0.12',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin': 'http://xggl.hnqczy.com',
               'Referer': 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_=1661311908508',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               }
    cookies = {
        'JSESSIONID':cooick1,
    }
    post_data = str("dkdz="+dkdz+
                    "&dkdzZb=111.795036,28.592264"
                    "&dkly=yiban"
                    "&zzdk_token="+str(jm())+
                    "&dkd="+dkd+
                    "&jzdValue=430000%2C430200%2C430202"
                    "&jzdSheng.dm=430000"
                    "&jzdShi.dm=430200"
                    "&jzdXian.dm=430202"
                    "&jzdDz=湖南汽车工程职业学院"
                    "&jzdDz2="+jzdDz2+
                    "&lxdh="+lxdh+
                    "&sfzx=1&sfzx1=%E5%9C%A8%E6%A0%A1"
                    "&twM.dm=01"
                    "&tw1=%5B35.0~37.2%5D%E6%AD%A3%E5%B8%B8"
                    "&tw1M.dm="
                    "&tw11="
                    "&tw2M.dm="
                    "&tw12="
                    "&tw3M.dm="
                    "&tw13="
                    "&yczk.dm=01"
                    "&yczk1=无症状"
                    "&fbrq="
                    "&jzInd=0"
                    "&jzYy="
                    "&zdjg="
                    "&fxrq="
                    "&brStzk.dm=01"
                    "&brStzk1=身体健康、无异常"
                    "&brJccry.dm=01"
                    "&brJccry1=未接触传染源"
                    "&jrStzk.dm=01"
                    "&jrStzk1=身体健康、无异常"
                    "&jrJccry.dm=01"
                    "&jrJccry1=未接触传染源"
                    "&jkm=1"
                    "&jkm1=绿色"
                    "&xcm=1"
                    "&xcm1=绿色"
                    "&xgym="
                    "&xgym1="
                    "&hsjc=1"
                    "&hsjc1="
                    "&bz="
                    "&operationType=Create"
                    "&dm=")
    post_data=post_data.encode('utf-8')
    rsp = requests.post(url,headers=headers, data=post_data,cookies=cookies).json()
    return rsp
xi=str(post_xxx())
if "True" in xi:
    tt = "打卡成功"
else:
    tt = '打卡失败'
print(tt)
# ----------------------------------------------------------推送--------------------------------------------------------------#
def ts():
    key = "填写"  # 微信推送key这里    链接获取#https://sct.ftqq.com/sendkey
    api = "https://sc.ftqq.com/" + key + ".send"
    data = {
        "title": str(tt),
        "desp":str(post_xxx())
    }
    reqq = requests.post(api, data=data).json()
    return reqq
print(ts())
def main_handler(event, context):
    if __name__ == '__main__':
        print("1")
