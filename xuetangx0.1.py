from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 

'''
启动Chrome并开启调试模式(powershell)：
./chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
'''
#data请自行在课程视频列表页抓包‘courseware'
data={"0769e9c5-f67a-4a8f-8afe-61e55d040170:f3d5f5aa-92bc-499f-8937-4e2a272bf360:137075": 54,
"0769e9c5-f67a-4a8f-8afe-61e55d040170:f1f88031-6cd0-4c6f-843a-365a1cba1c0b:137077": 55,
"0769e9c5-f67a-4a8f-8afe-61e55d040170:c98c654b-4ba0-4fa8-b05f-dd82f08f9c9f:137078": 56,
"0769e9c5-f67a-4a8f-8afe-61e55d040170:f01c0560-e156-4fc5-9e16-e0cfddc71e1e:137079": 57,
"0769e9c5-f67a-4a8f-8afe-61e55d040170:a9cb13f0-f911-4f4c-81cc-42b35ee28b43:137080": 58,
"0769e9c5-f67a-4a8f-8afe-61e55d040170:H+36049+017": 59,     #date like this (and also 62,66,72,76) are useless, it's not necessary to paste them here
"87e64b71-5a09-48ac-be18-ca83fed94d4b:4e30824d-5d34-48f9-a000-e3f4fde01079:137082": 60,
"87e64b71-5a09-48ac-be18-ca83fed94d4b:75edf904-ac8a-4f13-b8f7-7d1338dc75a1:137083": 61,
"87e64b71-5a09-48ac-be18-ca83fed94d4b:H+36049+018": 62,
"e30cd4e2-299b-48d2-bc86-dfe75779ccec:7782ed6b-65ae-4cbc-8d51-dff42bd46d0a:137084": 63,
"e30cd4e2-299b-48d2-bc86-dfe75779ccec:7c9598bf-450c-41b6-87c9-90c7fa78915c:137085": 64,
"e30cd4e2-299b-48d2-bc86-dfe75779ccec:360f8a0b-6b69-4e36-8076-7eb8555eb1c6:137086": 65,
"e30cd4e2-299b-48d2-bc86-dfe75779ccec:H+36049+019": 66,
"e32ff190-28a4-4bc5-af2e-786fcc919873:610d1d73-de83-48c0-a156-63062bb8d72c:137087": 67,
"e32ff190-28a4-4bc5-af2e-786fcc919873:a65ba3e5-df06-4e1d-839d-1d744a958735:137088": 68,
"e32ff190-28a4-4bc5-af2e-786fcc919873:cddd5d1e-8cc4-45c4-89ec-48b86da5479c:137089": 69,
"e32ff190-28a4-4bc5-af2e-786fcc919873:f53b8694-1ea0-421a-93a9-e0ce68ed51da:137090": 70,
"e32ff190-28a4-4bc5-af2e-786fcc919873:b53f79a2-24f5-4024-9393-20ed7f8a6cd9:137091": 71,
"e32ff190-28a4-4bc5-af2e-786fcc919873:H+36049+020": 72,
"6c42db0e-4934-4c61-bd5f-5be63944b946:84ce11cb-57c0-4e48-bc4a-e7504a552922:137092": 73,
"6c42db0e-4934-4c61-bd5f-5be63944b946:0407fc16-fa0b-4912-a4f0-dd6958acd4e1:137093": 74,
"6c42db0e-4934-4c61-bd5f-5be63944b946:fbe4953f-621c-4098-afbb-5ba9cb2a0df8:137094": 75,
"6c42db0e-4934-4c61-bd5f-5be63944b946:H+36049+021": 76}

def getkey(dct,value):
    return list(filter(lambda k:dct[k]==value,dct))

def clickinc(chapter):
    cxpath=str('/html/body/div[3]/div/div[2]/div[2]/section[2]/div/div/div/ul/li[')+str(chapter)+str(']/div[1]/span/span')
    celement=driver.find_element_by_xpath(cxpath)
    celement.click()

def clickinv(range0,range1,chapter):    #range1要求为最后一个视频代号+1
    for i in range(range0,range1):
        driver.get('https://scutspoc.xuetangx.com/lms#/36***/77***/schedule')
        #replace the url above with your coureslist
        sleep(5)
        if i==range0:
            clickinc(chapter)
        cid=getkey(data,i)[0]
        xpath=str('//*[@id="')+str(cid)+str('"]/div/a/span')
        
        element=driver.find_element_by_xpath(xpath)
        element.click()
        #ftime=driver.find_element_by_xpath('//*[@id="video-box"]/div/div/div[1]/div[2]/span[2]')
        sleep(720)
'''
cid=getkey(data,56)[0]
xpath=str('//*[@id="')+str(cid)+str('"]/div/a/span')
'''
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
chrome_driver ="C:\Program Files (x86)\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.get('https://scutspoc.xuetangx.com/lms#/36***/77***/schedule')
#replace the url above with your coureslist url
sleep(5)

clickinv(69,72,4)




#element=driver.find_element_by_link_text('1.')
#element=driver.find_element_by_class_name("element-title-detail")
#element=driver.find_element_by_xpath(xpath)
#element.click()




#print(cid)





#courselist=list(data.keys())[list(data.values()).index(' 56')]







