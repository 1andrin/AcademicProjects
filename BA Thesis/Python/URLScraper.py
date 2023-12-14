
##PREAMBLE
##DRIVER SETTING

import pandas as pd

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup as soup

import time

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

#from fake_useragent import UserAgent
#ua = UserAgent()
#userAgent = ua.firefox
#print(userAgent)

options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
chrome_driver_binary = "C:/Users/Andrin/Documents/PY SCRAPING/chromedriver.exe"
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

#################################################################

df = pd.read_csv(r"MissingURLs.csv")

parents = df['conml'].tolist()

df["url"] = None

print(len(parents))

#################################################################

for index, comp in enumerate(parents):

#get list of urls for parent.

  if "&" in comp:
    comp = comp.replace("&","%26")

  #url =  "https://www.google.ch/search?q=" + comp

  url = "https://www.bing.com/search?q=" + comp


  print("FIRM ", index+1, " out of ", len(parents), " ", round((index+1)*100/len(parents),1), " %", " URL: ", url)

  driver.get(url)

  time.sleep(5)

  urls = driver.find_elements(By.CSS_SELECTOR, "h2 > a")

#append urls into list called links

  links = []

  for l in urls:

    links.append(l.get_attribute('href'))

  df["url"][index] = links


df.to_csv("MissingURLs_COMPLETE.csv", encoding = "utf-8")