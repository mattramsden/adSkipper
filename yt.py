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

time.sleep(2)


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
                if (next.text == "Up Next"):
                    nextbut = browser.find_element_by_class_name(
                        'ytp-next-button')
                    nextbut.click()
            except NoSuchElementException:
                pass
            skip = browser.find_element_by_class_name('ytp-ad-skip-button')

            if(skip.text == "Skip Ads" or skip.text == "Skip Ad"):
                skip.click()
                print("clicked")
                break
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(1)
            pass


while True:
    try:
        try_skip()
    except NoSuchElementException:
        time.sleep(1)
        pass
exit(0)
