# -*- coding: utf-8 -*-
from selenium import webdriver
import random
import time

state="nowe" #new products only
offer_type="kup teraz" #buy now format only
max_number_subpages=3

def pause():
    paus = random.randint(9500,11073)
    time.sleep(paus/1000)

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)

#url containing soy&candle products
url="https://allegro.pl/kategoria/swiece-i-swieczniki-swiece-254295?stan=nowe&offerTypeBuyNow=1&string=sojowa&order=qd"

driver.get(url)
#service's internal add: required manual decision
pause() 
   
for subpage_no in range(1,max_number_subpages):
    item_list = driver.find_elements_by_xpath("//div[@class='_00d6b80']")                       
    for item in item_list:
        header=item.find_element_by_class_name("ebc9be2").text
        item_offers_no=item.find_element_by_xpath('.//span[@class = "_41ddd69"]').get_attribute('innerHTML')
        price=item.find_element_by_xpath('.//span[@class = "fee8042"]').text        
        link = item.find_element_by_css_selector('h2.ebc9be2>a').get_attribute('href')
        print(header + ' | ' + item_offers_no + ' | ' + price + ' | ' + link)
    #hit 'Next' subpage if possible
    current_subpage_no=driver.find_element_by_xpath("//input[@class='_14uqc _1r8rh _u5o1q _1t9p2 _cc6ig _3db39_3ISNX']").get_attribute('value')
    subpages_total_no=driver.find_element_by_xpath("//span[@class='_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE']").text
    if current_subpage_no==subpages_total_no:
        break
    else:
        driver.find_element_by_xpath("//span[@class='_lsy4e _1y3c2 _3db39_mcaVQ _ls4gg']").click()
        pause()
