#a
# from bs4 import BeautifulSoup
import pandas as pd
import re
import os
from selenium import webdriver
from time import sleep
# import bs4
import openpyxl
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chromedriver = "C:\\Users\\Project\\Downloads\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
driver = webdriver.Chrome(chromedriver)#, options=op)


for root, dirs, files in os.walk('D:\Amir\ynet'):
    for file in files:
        print("reading:", file)
        cntt = open('D:\Amir\ynet\\'+file, 'r', encoding='utf-8')
        lns = cntt.readlines()
        for ln in lns:
            ur = ln[:-2]
            try:
                driver.get(ur)
                sleep(1)
                try:
                    talkbacks = driver.find_element_by_class_name('art_tkb_talkback_title')
                    for i in list(range(1, 100)):

                        # username_box = driver.find_element_by_id('email')
                        # if i % 10 == 0:
                        #     print(i)
                        driver.execute_script("window.scrollBy(0, window.innerHeight)")
                    src_ = driver.page_source
                    file_2 = open("ynet_"+file, 'w', encoding='utf-8')
                    # file = open("ynet_2"+pth+"_.txt", 'w', encoding='utf-8')
                    file_2.write(src_)
                    file_2.close()
                    file_3 = open("ynet_"+file, 'r', encoding='utf-8')
                    # file = open("ynet_"+pth+"_.txt", 'r', encoding='utf-8')
                    content = file_3.readlines()
                    for line in content:
                        if 'art_tkb_talkback_title' in line:
                            talkbacks = line
                            result = re.findall("(?<=art_tkb_talkback_title).*$", talkbacks)#.group(0)  # oajrlxb2
                            result = re.findall(r'art_tkb_talkback_title.+?art_tkb_talkback_title',talkbacks)

                            # result = [el.split('</span><div class="art_tkb_name_location_date">')[0] for el in talkbacks.split('art_tkb_talkback_title') if '</span><div class="art_tkb_name_location_date">' in el]
                            result = [el.split('</span>')[0].replace('<span class="art_tkb_talkback_title_notkb">&nbsp;(לת)','') for el in talkbacks.split('art_tkb_talkback_title\">') if '</span><div class="art_tkb_name_location_date">' in el]
                            print(result)
                            # result = re.findall(".*art_tkb_talkback_title.*\n", talkbacks).group(0)  # oajrlxb2
                            continue
                except:
                    pass
            except:
                pass
pth = "https://www.ynet.co.il/articles/0,7340,L-5667706,00.html"
#
# # driver.add_argument('headless')
driver.get(pth)
# driver.get('https://www.facebook.com/')
# print("Opened facebook")
sleep(1)

# username_box = driver.find_element_by_id('email')
# username_box.send_keys('ami.rico@hotmail.com')
# username_box.send_keys(usr)
# print("Email Id entered")
sleep(1)

talkbacks = driver.find_element_by_class_name('art_tkb_talkback_title')

for i in list(range(1, 100)):

    # username_box = driver.find_element_by_id('email')
    # if i % 10== 0:
    #     print(i)
    driver.execute_script("window.scrollBy(0, window.innerHeight)")
src_ = driver.page_source
file = open("ynet_2.txt", 'w', encoding='utf-8')
# file = open("ynet_2"+pth+"_.txt", 'w', encoding='utf-8')
file.write(src_)
file.close()


file = open("ynet_2.txt", 'r', encoding='utf-8')
# file = open("ynet_"+pth+"_.txt", 'r', encoding='utf-8')
content = file.readlines()
for line in content:
    if 'art_tkb_talkback_title' in line:
        talkbacks = line
        result = re.findall("(?<=art_tkb_talkback_title).*$", talkbacks)#.group(0)  # oajrlxb2
        result = re.findall(r'art_tkb_talkback_title.+?art_tkb_talkback_title',talkbacks)

        # result = [el.split('</span><div class="art_tkb_name_location_date">')[0] for el in talkbacks.split('art_tkb_talkback_title') if '</span><div class="art_tkb_name_location_date">' in el]
        result = [el.split('</span>')[0].replace('<span class="art_tkb_talkback_title_notkb">&nbsp;(לת)','') for el in talkbacks.split('art_tkb_talkback_title\">') if '</span><div class="art_tkb_name_location_date">' in el]
        print(result)
        # result = re.findall(".*art_tkb_talkback_title.*\n", talkbacks).group(0)  # oajrlxb2
        continue



# usr = input('ami.rico@hotmail.com')
# pwd = input('')


# file = open('ynet_2.txt', 'r',encoding='utf-8')
# cntnt = file.read()
# result = re.search(".*gs-title.*\n", cntnt).group(0)  # oajrlxb2




chromedriver = "C:\\Users\\Project\\Downloads\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
driver = webdriver.Chrome(chromedriver)#, options=op)

driver.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")
# driver.get("https://www.ynet.co.il/home/0,7340,L-9600,00.html?q=%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D&cx=006008599374685598470:cb3lybzjt_k&cof=GIMP:009900;T:000000;ALC:FF9900;GFNT:B0B0B0;LC:0000FF;BRC:FFFFFF;BGC:FFFFFF;VLC:666666;GALT:36A200;LBGC:FF0000;DIV:FFFFEE;FORID:9;&as_qdr=all&hq=more:recent4&ynet_search_type=ynet")
# src_ = driver.page_source
# file = open('ynet_3.txt', 'w',encoding='utf-8')
# file.write(src_)
# file.close()
#
# result = re.search(".*gs-title.*\n", src_).group(0)  # oajrlxb2
# <input alt="חיפוש" class="mainSrchclass" id="mainSrchBox" aria-label="חיפוש" type="text" placeholder="" value="">
search_box = driver.find_element_by_class_name('mainSrchclass')
search_box.send_keys('ירושלים')
sleep(3)
# login_box = driver.find_element_by_class_name(('dyother dyMonitor'))#.find_element_by_id('login')
login_box = driver.find_element_by_id('MsBtn')#.find_element_by_id('login')
# login_box = driver.find_element_by_id('loginbutton')
login_box.click()
sleep(3)
search_box = driver.find_element_by_class_name('mainSrchclass')
search_box.send_keys(' ברזאני')
# driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])
driver.get(driver.current_url)
text = driver.find_element_by_tag_name("body").text

html1 = driver.execute_script("return document.body.innerHTML")
html2 = driver.execute_script("return document.documentElement.outerHTML")

src_ = driver.page_source
try_ = driver.find_element_by_class_name('gs-title')
file = open('ynet_4.txt', 'w',encoding='utf-8')
file.write(src_)
file.close()


try:
    result = re.search(".*gs-title.*\n", src_).group(0)  # oajrlxb2
except:
    print("not found")

# username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

# driver.add_argument('headless')
# driver.get("https://www.ynet.co.il/articles/0,7340,L-5667706,00.html")
# driver.get('https://www.facebook.com/')
# print("Opened facebook")
# sleep(1)

# username_box = driver.find_element_by_id('email')
# username_box.send_keys('ami.rico@hotmail.com')
# username_box.send_keys(usr)
# print("Email Id entered")
# sleep(1)

# talkbacks = driver.find_element_by_class_name('art_tkb_talkback_title')

# for i in list(range(1, 100)):
#
#     # username_box = driver.find_element_by_id('email')
#     if i % 10== 0:
#         print(i)
#     driver.execute_script("window.scrollBy(0, window.innerHeight)")
# src_ = driver.page_source
# file = open("ynet.txt", 'w', encoding='utf-8')
# file.write(src_)
# file.close()

file = open("ynet.txt", 'r', encoding='utf-8')
content = file.readlines()
file.close()


# soup = bs4.BeautifulSoup(content, 'lxml')
# x = soup.findAll('class')
# mydivs = soup.findAll("div", {"class": "art_tkb_talkback_title"})
talkbacks = ''
for line in content:
    if 'art_tkb_talkback_title' in line:
        talkbacks = line
        result = re.findall("(?<=art_tkb_talkback_title).*$", talkbacks)#.group(0)  # oajrlxb2
        result = re.findall(r'art_tkb_talkback_title.+?art_tkb_talkback_title',talkbacks)

        # result = [el.split('</span><div class="art_tkb_name_location_date">')[0] for el in talkbacks.split('art_tkb_talkback_title') if '</span><div class="art_tkb_name_location_date">' in el]
        result = [el.split('</span>')[0].replace('<span class="art_tkb_talkback_title_notkb">&nbsp;(לת)','') for el in talkbacks.split('art_tkb_talkback_title\">') if '</span><div class="art_tkb_name_location_date">' in el]

        # result = re.findall(".*art_tkb_talkback_title.*\n", talkbacks).group(0)  # oajrlxb2
        continue

# result = content[:10000].split('art_tkb_talkback_title')
result = re.search(".*art_tkb_talkback_title.*\n", content)#.group(0)  # oajrlxb2


df = pd.DataFrame([], columns=['name', 'profile'])

for root, dirs, files in os.walk('D:\FBScraper\profiles'):
    for file in files:
        print('D:\\FBScraper\\profiles\\'+file)
        file_object = open('D:\\FBScraper\\profiles\\'+file, 'r', encoding='utf-8')
        content = file_object.read()
        result = re.search(".*oajrlxb2.*\n", content).group(0)#oajrlxb2
        result  = result.replace("<div class=\"nc684nl6\">","\n<div class=\"nc684nl6\">")
        sents = [re.sub('\" role.*','',el.replace('<div class="nc684nl6"><a aria-label="',"").replace('" class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8" href="','\t')) for el in result.split("\n") if '<div class="nc684nl6"><a class="oajrlxb2' not in el and '<div class="nc684nl6"><a aria-label="' in el]
        sents = [(el.split("\t")[0],el.split("\t")[1]) for el in sents]
        local_df = pd.DataFrame(sents, columns=['name', 'profile'])
        result  = result.replace("<div class=\"nc684nl6\"><a class=\"oajrlxb2[ a-z0-9]*\n","-----------------------------------")
        df.append(local_df)
        df = pd.concat([local_df, df])
        # result  = result.replace("<div class=\"nc684nl6\"><a class=\"oajrlxb2 .*\\n","")

        # print(content)


df = df.reset_index()[['name','profile']].drop_duplicates()
df.to_excel("members.xlsx")

# ['Anna','Marina','Olga','Yulia','Alex','Elena','Inna','Michael', ['Ira','Yana','Maria','Daniel','Ella','Lena','Alina','Irina','Michal','Tanya','Diana','David','Dana','Ilana','Julia','Maya','Alona','Irena','Anastasia','Victoria',
#  'Yael','Sharon','Jenny','Polina','Alexandra','Sveta','Alla','Miri','Natali','Orit','Alexander','Anat','Katya','Rita','Svetlana','Adi','Dima','Eli','Ilona','Liza','Masha','Noa','Revital','Keren','Larisa','Nataly','Tali','Vika',
#  'Boris','Einat','Igor','Lior','Natalia','Natalie','Tatyana','Daria','Evgeny','Tal','Alon','Ariel','Dina','Guy',
names = ['Karina','Lina','Mila','Rachel','Regina','Sasha','Avi','Avital','Bella','Eden','Galit','Liora','Oksana','Olya',
 'Roman','Tamara','Vladimir','Yelena','Anton','Chen','Darya','Igal','Ilia','Ilya','Karin','Katy','Kristina','Liat','Mark','Mor','Nir','Oleg','Sabina','Shelly','Sigal','Sivan','Tamar','Viki','Andrey','Efrat','Elina','Gal',
 'Galina','Hadar','Hila','Ilan','Janna','Moshe','Nikol','Nina','Noam','Oren','Sergey','Valeria','Yuli','Yuri','Alin','Amir','Bar','Dan','Ela','Elizabeth','Gali','Jenia','Leonid','Luda','Max','Misha','Naomi','Neta','Orly',
 'Rina','Ronit','Sandra','Shiran','Tania','Tomer','Yaniv','Alisa','Amit','Anya','Dalia','Daniela','Ekaterina','Felix','Idan','Margarita','Mishel','Nadia','Natalya','Natasha','Raya','Ron','Ronen','Roni','Sofi','Sofia','Sophie',
 'Stas','Tatiana','Valentina','Vera','Veronika','Yarden','Arie','Aviv','Aya','Ben','Danielle','Danny','Denis','Eran','Erez','Faina','Galia','Gil','Hagit','Inga','Iris','Jonathan','Kira','Ksenia','Lev','Liel','Liron','Lora',
 'Luba','Maayan','Mariya','Maxim','Michelle','Moran','Nadya','Nastia','Nastya','Nicole','Ofer','Ofir','Or','Pnina','Rinat','Ruth','Sara','Sarit','Shai','Shani','Sharona','Shimon','Shir','Talia','Uri','Vadim','Vicky','Vita',
 'Yehuda','Yoni','Yossi','Yuliya','Zoya','Alice','Anastasiya','Anastasya','Angela','Asaf','Asia','Benny','Boaz','Daniella','Ehud','Elad','Eliran','Ester','Esther','Esty','Eyal','Hadas','Hanna','Hava','Ida','Inbal','Irit',
 'Jana','Jenya','Katia','Katrin','Lea','Lee','Lilia','Liran','Lital','Marianna','Milana','Milena','Miriam','Naama','Nataliya','Niv','Ohad','Orna','Pavel','Shay','Shira','Shirley','Simona','Slava','Sophia','Stella','Tom',
 'Veronica','Viktoria','Yan','Yaron','Adam','Amichai','Anastassia','Angelina','Anita','Ann','Arina','Artem','Artur','Asya','Ayelet','Bat-Sheva','Batya','Carmit','Christina','Dafna','Dani','Dmitry','Dor','Dora','Dorit',
 'Doron','Dudu','Edi','Elinor','Emilia','Eti','Eugene','Evgenia','Genia','Gennady','Gila','Gilad','Gleb','Haya','Helen','Inbar','Irene','Jacob','Jeny','Kirill','Klara','Kobi','Lana','Leah','Leon','Li','Lia','Lika','Lili',
 'Liliya','Lin','Linda','Linor','Liz','Madina','Maor','Mariana','Meir','Meital','Mike','Miki','Mina','Mira','Moti','Nati','Netanel','Nili','Nisim','Nofar','Noga','Noy','Ola','Olesya','Omri','Ortal','Oxana','Racheli','Rami',
 'Ran','Rena','Rima','Rotem','Roy','Roza','Sami','Sergei','Shahar','Shiri','Shirly','Shlomit','Sonia','Sonya','Tami','Valeriya','Vered','Victor','Viktoriya','Vitaly','Vlada','Vova','Yair','Yasmin','Yonatan']

#
# name = 'Yael'

chromedriver = "C:\\Users\\Project\\Downloads\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
driver = webdriver.Chrome(chromedriver)#, options=op)
# driver.add_argument('headless')
driver.get("https://www.facebook.com/groups/781518758549418/members")
# driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys('ami.rico@hotmail.com')
# username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')#stlkbc72400342tsurrdiv > a > div.art_tkb_talkback_title > div.art_tkb_talkback_details_inner > span
password_box.send_keys('')
print("Password entered")

login_box = driver.find_element_by_name(('login'))#.find_element_by_id('login')
# login_box = driver.find_element_by_id('loginbutton')
login_box.click()

sleep(5)
class_="oajrlxb2 rq0escxv f1sip0of hidtqoto lzcic4wl ijkhr0an nlq1og4t sgqwj88q b3i9ofy5 oo9gr5id b1f16np4 hdh3q7d8 dwo3fsh8 qu0x051f esr5mh6w e9989ue4 r7d6kgcz br7hx15l h2jyy9rg n3ddgdk9 owxd89k7 ihxqhq3m jq4qci2q k4urcfbm iu8raji3 tv7at329 l60d2q6s d1544ag0 hwnh5xvq tw6a2znq o1lsuvei"
# driver.findElement(By.xpath("//input[@class='form-control date-type']")).sendKeys("06/24/2017");
srch = driver.find_element_by_xpath("//input[@class='"+class_+"']")
# srch.send_keys('Yael')
for name in names:
    srch.send_keys(name)
    driver.execute_script("window.scrollTo(0,5550)")
    # srch = driver.find_element_by_class_name('n1l5q3vz')

    # srch_ = driver.find_element_by_css_selector('Search Group Members')
    # .send_keys("Yael")
    # srch = driver.find_element_by_link_text()
    n = 3000
    sleep(5)
    for i in list(range(1,n)):

        # username_box = driver.find_element_by_id('email')
        if i%1000 == 0:
            print(i)
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
    # driver.execute_script("window.scrollBy(0, window.innerHeight)")
    # for i in list(range(1,n)):
    #     driver.execute_script("window.scrollBy(0, window.innerHeight)")
    # for i in list(range(1,n)):
    #     driver.execute_script("window.scrollBy(0, window.innerHeight)")
    print("Done")
    src_ = driver.page_source
    srch.clear()
    # srch.send_keys('Irena')
    file = open(name+"_named_profiles.txt", "w", encoding='utf-8')
    file.write(src_)
    file.close()
input('Press anything to quit')
driver.quit()
print("Finished")


import os
from selenium import webdriver

chromedriver = "C:\\Users\\Project\\Downloads\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.facebook.com/groups/781518758549418/members")
driver.execute_script("window.scrollTo(0,550)")
import bs4
import threads
import members
import json

cookieText = "C%7B%22t3%22%3A%5B%7B%22i%22%3A%22g.1934907093300015%22%7D%2C%7B%22i%22%3A%22g.3770130456338570%22%7D%2C%7B%22i%22%3A%22g.1934907093300015%22%7D%2C%7B%22i%22%3A%22g.4762922130388334%22%7D%2C%7B%22i%22%3A%22g.3770130456338570%22%7D%2C%7B%22i%22%3A%22g.4762922130388334%22%7D%2C%7B%22i%22%3A%22g.3239053846187006%22%7D%2C%7B%22i%22%3A%22g.3770130456338570%22%7D%2C%7B%22i%22%3A%22u.523967902%22%7D%2C%7B%22i%22%3A%22u.1356514042%22%7D%2C%7B%22i%22%3A%22u.1040932878%22%7D%2C%7B%22i%22%3A%22u.100002457555006%22%7D%2C%7B%22i%22%3A%22g.3376003955795105%22%7D%2C%7B%22i%22%3A%22u.1395684244%22%7D%2C%7B%22i%22%3A%22u.100002352538570%22%7D%2C%7B%22i%22%3A%22u.100000081878457%22%7D%2C%7B%22i%22%3A%22u.770878604%22%7D%2C%7B%22i%22%3A%22u.1408436657%22%7D%2C%7B%22i%22%3A%22u.1742570443%22%7D%2C%7B%22i%22%3A%22g.3431727600205463%22%7D%2C%7B%22i%22%3A%22g.3981262378554699%22%7D%2C%7B%22i%22%3A%22g.4149637415109999%22%7D%2C%7B%22i%22%3A%22g.3128177917289080%22%7D%2C%7B%22i%22%3A%22g.3308200575933834%22%7D%2C%7B%22i%22%3A%22g.4724047104302703%22%7D%2C%7B%22i%22%3A%22g.3193927467364427%22%7D%2C%7B%22i%22%3A%22g.4330862450289776%22%7D%2C%7B%22i%22%3A%22g.4452745128099342%22%7D%2C%7B%22i%22%3A%22g.4019084994787160%22%7D%2C%7B%22i%22%3A%22g.3395205860531487%22%7D%2C%7B%22i%22%3A%22u.580510206%22%7D%5D%2C%22utc3%22%3A1597997755392%2C%22v%22%3A1%7D"
groupId = "781518758549418"

# print(1)
# threads = threads.Thread(groupId, cookieText)
# data = threads.getDict()
# threadJson = json.dumps(data, indent=4, sort_keys=True)
#
# members = members.Member(groupId, cookieText)
# data = members.getDict()
# memberJson= json.dumps(data, indent=4, sort_keys=True)
#
# with open('members.json', 'w') as outfile:
#     outfile.write(memberJson)
#
# with open('threads.json', 'w') as outfile:
#         outfile.write(threadJson)