# Presearch-bot

### Hi there,  
### Presearch-bot is designed for automatically search Presearch.org for PRE token on firefox and Linux (Kali).

![image](https://github.com/a13x4ack/Presearch-bot/blob/main/PresearchBot.gif)

---
### Build environmennt.
1. Kali / Linux   
2. [Install Python Selenium](https://selenium-python.readthedocs.io/installation.html)
```
sudo apt-get install python-pip
```
```
python -m pip install selenium
```

3. [Install Geckodriver](https://github.com/mozilla/geckodriver/releases)
* I downloaded - [geckodriver-v0.30.0-linux64.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz)
4. Extract Geckodriver & move to Bin folder
```
tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
```
```
sudo cp geckodriver /usr/local/bin 
```
---

### Create Presearch account and save to firefox profile. 

1. [(Crtl+Click) Create Presearch.org account](https://presearch.org/signup?rid=3692934) > make sure the account save in your firefox default.
2. [Do manual search on Presearch.org at first](https://presearch.org/signup?rid=3692934)> avoid login problem  
**[Important]**  
Sometime, even you login on the presearch home page, you account won't be connected successful during searching then you can not get PRE token reward. 

![image](https://github.com/a13x4ack/Presearch-bot/blob/main/Tricky-FirstSearchwithoutlogin.jpg)  
3.  Check the path of your firefox profile
```
cd ~/.mozilla/firefox && ls -a
```
4. Modify the code of firefox profile to point to yours. 
![image](https://github.com/a13x4ack/Presearch-bot/blob/main/ModifyPathOfFirefoxProfile-.jpg)

5. Save & Run
```
python presearchbot.py
```

### Advance & Others
1. You can do your own dynamic searchlist.txt let the whole process looks like human being.   
2. You can use different firefox profiles for multi-account for multi-process to maximize your profit. As my experience. There is no problem earning up to 600 PRE per day.

Enjoy.

Create Presearch.org account >> https://presearch.org/signup?rid=3692934


