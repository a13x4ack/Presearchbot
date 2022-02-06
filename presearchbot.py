#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Hi there, 
This script is for automated firefox web browser search on presearch.org.


1. click url: https://presearch.org/signup?rid=3692934 to create an presearch account(and learn 25 PRE) 

2. Install Selenium. You can install it from here:  https://presearch.org/signup?rid=3692934 

3. 


"""

import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOME_DIRECTORY = os.environ.get('HOME')

options = webdriver.FirefoxOptions()

options.add_argument("--width=800");

options.add_argument("--height=640");

profile = webdriver.FirefoxProfile(HOME_DIRECTORY + "/.mozilla/firefox/784s2sg4.presearch")

options.binary_location = "/usr/bin/firefox"

browser = webdriver.Firefox(firefox_profile=profile,firefox_options=options)

def dosearch(searcheditem):

	#time.sleep(10)

	print("Open the presearch... \n")

	browser.get("https://www.presearch.org/?utm_source=extcr")

	try:
	    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "search")))
	finally:
		print("Search... " + searcheditem + "\n")
		element.send_keys(searcheditem, Keys.ENTER)

	time.sleep(10)

list = open("search1.txt", "r")

for searcheditem in list.readlines():
	dosearch(searcheditem)

browser.close()

__author__ = "Erick Carvajal"
__copyright__ = "Copyright 2019, presearch.py"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "@neocarvajal"
__email__ = "neocarvajal@gmail.com"
__status__ = "Production"
