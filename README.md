# Presearch-bot

Hi there,  
This script is used to automatically search Presearch.org on firefox and Linux (Kali) to earn PRE token.

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

1. [(Crtl+Click) Create Presearch.org account](https://presearch.org/signup?rid=3692934) - make sure the account save in your firefox default.
2. [Do manual search on Presearch.org at first](https://presearch.org/signup?rid=3692934)-Important, First time, even you login on the presearch home page, you account will be connected during searching then you cannot get PRE token reward. 
3. Check your firefox profile
4. Modify the code of firefox profile which can point to yours. 
5. Save & Run

```
python xxxxxxxx.py
```

