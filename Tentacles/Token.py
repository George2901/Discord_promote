from random import randint
from time import sleep
from tokenize import String
from xmlrpc.client import Boolean

import requests
import undetected_chromedriver.v2 as uc
from bs4 import BeautifulSoup
from undetected_chromedriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

try:from .Link import LINK
except:from Link import LINK



def get_name() -> str:
    def mTvuGv():
        soup = requests.get(LINK)
        parser = BeautifulSoup(soup.text, 'html.parser')
        mydivs = parser.find_all("div", {"class": "random-results"})
        forge:str = mydivs[0].getText()
        forge:str = forge.lower()
        forge:str = forge.replace(' ','')
        a = f'{randint(0,9)}{randint(0,9)}'
        return f'{forge}{a}'

    while(True):
        return_string = mTvuGv()
        if len(return_string) >= 15:
            pass
        else:
            return return_string

def get_xelem(driver:Chrome, xpath:String):
    while(True):
        elem = None
        try:elem = driver.find_element_by_xpath(xpath)
        except Exception as e:print(e)
        else:
            elem.click()
            break
        sleep(1)
    return elem

def get_idelem(driver:Chrome, id:String):
    while(True):
        elem = None
        try:elem = driver.find_element_by_id(id)
        except Exception as e:print(e)
        else:elem.click();break
        sleep(1)
    return elem

def main():
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  
    options = uc.ChromeOptions()
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic --no-sandbox')
    
   
    global driver
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://discord.com/')

    get_xelem(driver, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button')#Goto web interface
    get_xelem(driver, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input')\
        .send_keys(get_name())#Username
    get_xelem(driver, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/div/div/div')#Bullshit
    get_xelem(driver, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button')#Submit
    
    input()
    
if __name__ == "__main__":
    main()
    
