#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Hi there,
Presearch-bot is designed for automatically search Presearch.org for PRE token on firefox and Linux (Kali).

MoreInfo: https://github.com/a13x4ack/Presearch-bot

Create Presearch Account to earn 25 PRE >> https://presearch.org/signup?rid=3692934 
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

"""Modify your path of Firefox Profile in here"""
profile = webdriver.FirefoxProfile(HOME_DIRECTORY + "/.mozilla/firefox/hav2k2rg.default-esr")

options.binary_location = "/usr/bin/firefox"
browser = webdriver.Firefox(firefox_profile=profile,firefox_options=options)

def dosearch(searcheditem):

	print("Open the Presearch.org ...")

	browser.get("https://www.presearch.org/?utm_source=extcr")

	try:
	    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "search")))
	finally:
		print("Search... " + searcheditem)
		element.send_keys(searcheditem, Keys.ENTER)

	time.sleep(10)

list = open("searchlist.txt", "r")

for searcheditem in list.readlines():
	dosearch(searcheditem)

browser.close()
