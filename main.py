from selenium import webdriver                   
from selenium.webdriver.common.keys import Keys
import time                         
from selenium.webdriver.support.ui import Select
browser = webdriver.Safari()  
browser.maximize_window()
URL = "https://leetcode.com/problemset/all/"
browser.get(URL)
time.sleep(5)

select = Select(browser.find_elements_by_class_name('form-control')[-1])
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
select.select_by_visible_text('all')
links = browser.find_elements_by_tag_name('a')
visit=[]
c=0
for i in links:
    t = str(i.get_attribute("href"))
    print(t)
    if 'problems/' in t:
        visit.append(t)

data =[]
errors=[]
total = len(visit)
for i,link in enumerate(visit):
    try:
        print("{}/{}".format(i,total),end=" ")
        browser.get(link)
        time.sleep(4)
        buttons = browser.find_elements_by_tag_name("button")
        el = browser.find_elements_by_class_name("css-dcmtd5") + browser.find_elements_by_class_name(
            "css-t42afm") + browser.find_elements_by_class_name("css-14oi08n")
        data.append((link, buttons[1].text, buttons[2].text, el[0].text))
        print()
    except:
        print("Couldn't visit {}".format(link))
        errors.append(i)
        pass
with open("leetcode_data.csv","w") as file:
    for link,like,dislike,diff in data:
        file.write("{},{},{},{}\n".format(link, like, dislike, diff))

with open("errors.csv", "w") as file:
    for link in errors:
        file.write("{}\n".format(link))
browser.close()
    

