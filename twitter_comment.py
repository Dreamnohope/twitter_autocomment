from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


def read_words():
    open_file = open('words.txt', 'r')
    wordslist = []
    contents = open_file.readlines()
    for i in range(len(contents)):
        wordslist.extend(contents[i].split())
    open_file.close()

    return wordslist


def select_word(words):
    rng = random.randint(1, len(words))
    print("Sent " + words[rng])
    return words[rng]


usr = 'Username'
pwd = 'Password'
login_url = 'https:/twitter.com/login'
tweet_url = 'tweet url'

driver = webdriver.Chrome('chromedriver location')
driver.get(login_url)

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name('js-password-field')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()
sleep(1)


i = 0
while i < 1000:
    i += 1
    sleep(1)
    driver.get(tweet_url)
    reply_box = driver.find_element_by_id('reply box ID')
    reply_box.send_keys(select_word(read_words()))
    sleep(.3)
    reply_box.send_keys(Keys.CONTROL + Keys.ENTER)
    print('Outputted ', i, 'words this session')


