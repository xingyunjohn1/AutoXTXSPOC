from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, strptime, mktime
from os import popen
from itertools import count
#该版本不完整，请跳到03版——思路修改
'''首次使用先启动浏览器
chromedir = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
port = 9222
datadir = 'C:\selenum\AutomationProfile'

cmdport = ' --remote-debugging-port=' + str(port)
cmddatadir = ' --user-data-dir="' + datadir + '"'
popen(str('"' + chromedir + '"' + cmdport + cmddatadir))
'''

print('Please wait...')
print('loading...')
#连接浏览器、打开学堂云
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
chrome_driver ="C:\Program Files (x86)\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.get('https://scutspoc.xuetangx.com/')
sleep(5)
#判断是否已登录
print('please login')
loginpath = '/html/body/div[1]/div[1]/div[1]/div/div/div[3]/ul/li/a'
'''#自动点击登录，但由于若已登录时、使用此代码块会报错，默认不启用
login = driver.find_element_by_xpath(loginpath)
if login.text == '登录':
    login.click()
'''
logEC = EC.text_to_be_present_in_element((By.XPATH,loginpath),u'登录')
WebDriverWait(driver,300,0.5).until_not(logEC)
print('login successfully')
print('loading...')
#判断是否进入课程页面
driver.get('https://scutspoc.xuetangx.com/manager#/studentcourselist')
while True:
    currentPageUrl = driver.current_url
    if currentPageUrl[-9:-1] == 'schedule':
        print('''已进入课程页面
loading...''')
        break
    else:
        print('请进入课程页面scutspoc.xuetangx.com/lms#/*/*/schedule/')
        listpath = '/html/body/div[1]/div[2]/div/div/div[2]\
/div/div/div/div/div/div[1]/div[1]/ul/li[1]/label'
        listEC = EC.text_to_be_present_in_element((By.XPATH,listpath),u'学期:')
        WebDriverWait(driver,300,0.5).until_not(listEC)
loadpath = '/html/body/div[3]/div/div[2]/div[2]/section[2]/div/div/div/div/p'
loadEC = EC.text_to_be_present_in_element((By.XPATH,loadpath),u'加载中,\
请稍候...')
WebDriverWait(driver,300,0.5).until_not(loadEC)    
#选定从 第begunit单元的第begv个 视频播放到 第endunit单元的第endv个视频
rawassign = input('''input begin unit&video and end unit&video
like '2,1,4,4'(default:'1,1,99,99'):''')
if rawassign == '':
    rawassign = '1,1,99,99'
key = ['begunit', 'begv', 'endunit', 'endv']
assign = {}
for i in range(4):
    assign[key[i]] = rawassign.split(',')[i]
#定义生成器，进行遍历
def countfrom(i):
    i = i - 1
    while True:
        i += 1
        yield i
#通过XPath获取视频地址，当遍历到尽头，except，实际返回None，原因未知        
def getvlink(unit,v):
    vpath = '/html/body/div[3]/div/div[2]\
/div[2]/section[2]/div/div/div/ul/li[{}]\
/div[2]/div/ul/li[{}]/div/ul/li/div/a'.format(unit,v)
    for link in driver.find_elements_by_xpath(vpath):
        try:
            #print('Unit{} video{}:'.format(unit,v),link.get_attribute('href'))
            return link.get_attribute('href')
        except:
            return 1


#按要求遍历需要的视频地址
linklist = []   
for unit in range(int(assign.get('begunit')),int(assign.get('endunit')) + 1):
    if unit == int(assign.get('endunit')):
        for v in range(1,int(assign.get('endv')) + 1):
            vlink = getvlink(unit,v)
            if vlink == None:
                break
            else:linklist.append(vlink)
    elif unit == int(assign.get('begunit')):
        for v in countfrom(int(assign.get('begv'))):
            vlink = getvlink(unit,v)
            if vlink == None:
                break
            else:linklist.append(vlink)
    else:
        for v in countfrom(1):
            vlink = getvlink(unit,v)
            if vlink == None:
                break
            else:linklist.append(vlink)
print(linklist)

for i in linklist:
    driver.get(i)
    sleep(3)
    chpath = '/html/body/div[3]/div/div[2]/div[2]/\
div/section[1]/div[2]/div[1]/div/div/div[1]/div[8]/div[1]'
    while True:
        try:
            ch = driver.find_element_by_xpath(chpath).get_attribute('text\
Content')
            if ch == u'字幕':
                print('loaded')
                break
        except:continue
    #chEC = EC.text_to_be_present_in_element((By.XPATH,chpath),u'字幕')
    #WebDriverWait(driver,300,0.5).until(chEC)
    lenpath = '/html/body/div[3]/div/div[2]/div[2]/\
div/section[1]/div[2]/div[1]/div/div/div[1]/div[2]/span[2]'
    pedpath = '/html/body/div[3]/div/div[2]/div[2]/\
div/section[1]/div[2]/div[1]/div/div/div[1]/div[2]/span[1]'
    rawvlen = driver.find_element_by_xpath(lenpath) #.text
    vlen = rawvlen.get_attribute('textContent')
    print(vlen)
    i = 2
    while i > 0:
        while True:
            try:
                ed = driver.find_element_by_xpath(pedpath).get_attribute('text\
    Content')
                if ed == vlen:
                    print('finished')
                    i -= 1
                    break
            except:continue
    #edEC = EC.text_to_be_present_in_element((By.XPATH,pedpath),vlen)
    #WebDriverWait(driver,300,0.5).until(edEC)
    print('finish')

'''        
        #link = driver.find_elements_by_xpath(vpath)
        #print(link.get_attribute('href'))
'''
driver.quit
