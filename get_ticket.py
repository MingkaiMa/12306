#coding=utf-8  
import time  
from splinter import Browser  
import re

def splinter(url):  
    browser = Browser('chrome')  
    #login 126 email websize  
    browser.visit(url)  
    #wait web element loading  
    time.sleep(1)  


    ##input username
    browser.find_by_tag('input')[0].fill('username')

    ##input password
    browser.find_by_tag('input')[1].fill('password')

    time.sleep(10)
    print('click now!')
    
    
    browser.find_by_id('loginSub').click()




    time.sleep(20)
    print('sleep')


    browser.find_by_xpath('//*[@id="selectYuding"]/a').first.click()
 
    time.sleep(0.5)



    print(browser.cookies.all())


    browser.cookies.add({'_jc_save_toStation':'%u90D1%u5DDE%2CZZF'})
    browser.cookies.add({'_jc_save_fromStation':'%u4E0A%u6D77%2CSHH'})

    browser.cookies.add({'_jc_save_fromDate':'2018-02-13'})
    browser.reload()
    print(browser.cookies.all())

    browser.find_by_xpath('//*[@id="query_ticket"]').first.click()

    time.sleep(0.5)





    target_line = ['G1952', 'G3600', 'G1866', 'G1806', 'G1920', 'G1924', 'G1956', 'G1810', 'G1928', 'G1814', 'G1932', 'G1818']


    flag = False
    while True:
        
        a_list = browser.find_by_tag('a')

        for a in a_list:


            if not a['onclick']:
                continue


            if 'checkG1234' in a['onclick']:
                L = a['onclick'].split(',')
                s = L[2]
                line = re.findall(r'G[0-9]{4}',s)

                if(len(line) != 0):
                    line_nb = line[0]
                
                    print(s,'-----', line_nb)
                    if line_nb in target_line:

                        s = s.strip("'")
                        id_target = 'ZE_' + s
                        print(id_target)
                        print(id_target.strip("'"))

                        available = browser.find_by_xpath(f'//*[@id="{id_target}"]/div')
                        print(available.text)

                        if(available.text == '无'):
                            continue
                        print(type(available.text))

                        
                        
                        print(line_nb)
                        print(a.text)
                        print('***')
                        a.click()
                        flag = True
                        break

                               
        if flag == True:
            print('found')
            break
        else:
            print('not found')

        browser.reload()
        browser.find_by_xpath('//*[@id="query_ticket"]').first.click()

    browser.find_by_xpath('//*[@id="normalPassenger_0"]').first.click()
    browser.find_by_xpath('//*[@id="normalPassenger_4"]').first.click()
    browser.find_by_xpath('//*[@id="submitOrder_id"]').first.click()    


    browser.click_link_by_id('query_ticket')


    
    time.sleep(8)

    

 
        
        


if __name__ == '__main__':  
    websize3 = 'https://kyfw.12306.cn/otn/login/init'  
    splinter(websize3)  
