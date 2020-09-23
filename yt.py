#! /usr/local/bin/python3
from urllib.parse import quote
from time import sleep
import time
from pyperclip import copy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from random import random
from random import randint
from datetime import datetime
import sys

input = str(sys.argv[1])
print("This is the link: " + input)
#input = input("Paste the URL of the video here: ")
file1 = open("_log.txt", "w+")
x = input[0]
print("jkjks: " + x)
print("rest" + input[1:])

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


browser = webdriver.Chrome(ChromeDriverManager().install())

QUIT = False
PRODUCTION = False
SCANNED = False
SCANNED1 = False
chats = "none"
HOST = 'http://localhost:3000'
CHANGE = False

if PRODUCTION is True:
    HOST = 'http://whatsapp-monitor.now.sh'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
)
browser.get(input)
#browser.get("https://www.youtube.com/watch?v=fcGEP1STu8M")
time.sleep(2)
#playlist = browser.find_element_by_id['video-title']
# playlist.click()
'''
search_bar = browser.find_elements_by_class_name('ytd-searchbox')[0]
search_bar.click()
search_bar = browser.find_elements_by_class_name('ytd-searchbox')[0]

search_bar.send_keys("music")
'''
try:
    overlay = browser.find_elements_by_class_name('ytp-large-play-button')[0]
    overlay.click()
except NoSuchElementException:
    pass


def try_skip():
    while True:
        try:
            try:
                next = browser.find_element_by_class_name("ytp-upnext-header")
                #(next.text)
                if (next.text == "Up Next"):
                    nextbut = browser.find_element_by_class_name('ytp-next-button')
                    nextbut.click()
            except NoSuchElementException:
                #print("not there")
                pass
            skip = browser.find_element_by_class_name('ytp-ad-skip-button')
            #print(skip.text)
            if(skip.text == "Skip Ads" or skip.text == "Skip Ad"):
                skip.click()
                print("clicked")
                break
            #print("tried")
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(1)
            #print("error")
            pass

while True:
    try:
        '''
        duration = browser.find_element_by_class_name(
            'ytp-time-duration').text
        current = browser.find_element_by_class_name(
            'ytp-time-current').text

        dur_min = duration[:1]
        dur_sec = duration[2:]

        curr_min = duration[:1]
        curr_sec = duration[2:]

        tdursec = int(dur_min*60) + int(dur_sec)
        tcurr = int(curr_min*60) + int(curr_sec)

        print(dur_min + ":" + dur_sec)


        if(tdursec - tcurr < 5):
            try_skip()
'''
        try_skip()
    except NoSuchElementException:
        time.sleep(1)
        pass





exit(0)
