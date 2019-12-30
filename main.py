from selenium import webdriver                   
from selenium.webdriver.common.keys import Keys
import time                         
from selenium.webdriver.support.ui import Select
browser = webdriver.Safari()  
browser.maximize_window()
URL = "https://leetcode.com/problemset/all/"
browser.get(URL)
time.sleep(5)

time.sleep(5)
select = Select(browser.find_elements_by_class_name('form-control')[-1])
time.sleep(5)
select.select_by_visible_text('all')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

links = browser.find_elements_by_tag_name('a')
visit=[]
for i in links:
    t = str(i.get_attribute("href"))
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
        data.append((link, buttons[1].text, buttons[2].text))
        print()
    except:
        print("Couldn't visit {}".format(link))
        errors.append(i)
        pass
with open("leetcode.csv","w") as file:
    for link,like,dislike,diff in data:
        file.write("{},{},{},{}\n".format(link, like, dislike, diff))

with open("errors.csv", "w") as file:
    for link in errors:
        file.write("{}\n".format(link))
    

