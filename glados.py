import requests,json,os
# -------------------------------------------------------------------------------------------
# 所有的变量都可以用环境变量代替，我自己是直接写到了脚本里。                                     -
# -------------------------------------------------------------------------------------------
# 推送开关 off/on
sever = 'off'
# pushplus秘钥 申请地址 http://www.pushplus.plus
sckey = os.environ.get("PUSHPLUS_TOKEN", '')
if sckey != ''
   sever = 'on'
# 推送内容
sendContent = ''
# glados账号cookie 直接使用数组 如果使用环境变量需要字符串分割一下
cookies = os.environ.get("COOKIES", []).split("&")
print(cookies) 
def start():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload={
        'token': 'glados.network'
    }
    for cookie in cookies:
        checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    #--------------------------------------------------------------------------------------------------------#  
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        email = state.json()['data']['email']
        if 'message' in checkin.text:
            mess = checkin.json()['message']
            print(email+'----结果--'+mess+'----剩余('+time+')天')  # 日志输出
            global sendContent
            sendContent += email+'----'+mess+'----剩余('+time+')天\n'
        else:
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email+'cookie已失效')
     #--------------------------------------------------------------------------------------------------------#   
    if sever == 'on':
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+email+'签到成功'+'&content='+sendContent)


if __name__ == '__main__':
    start()
