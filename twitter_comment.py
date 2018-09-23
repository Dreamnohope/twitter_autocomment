from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


def read_words(file_name):
    file = open(file_name, 'r')
    wordslist = []
    for line in file:
        if line is not '\n':
            wordslist.append(line.strip())
    file.close()
    # contents = open_file.readlines()
    # for i in range(len(contents)):
    #     c = contents[i].strip()
    #     wordslist.append(c.split())
    #     # wordslist.append(contents[i].strip().split(','))
    #     # wordslist = [x.replace('\n', '') for x in rawlist] # removes \n
    #     # wordslist.extend(contents[i].strip('\n').split(','))  # this splits the list by spaces
    
    file.close()
    return wordslist


def words_length(file_name):
    open_file = open(file_name, 'r')
    words = open_file.readlines()
    return len(words)


def select_word(words):
    rng = random.randint(1, len(words))
    print("Sent " + words[rng])
    return words[rng]


randomornot = input('Random?')
filename = input('File name...')
usr = 'usr'
pwd = 'passwoed'
login_url = 'https:/twitter.com/login'
tweet_url = input('Tweet url?')

driver = webdriver.Chrome('chromedriver')
driver.get(login_url)

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name('js-password-field')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()
sleep(1)


i = 0
j = 0
while i < words_length(filename):
    i += 1
    sleep(1)
    driver.get(tweet_url)
    reply_box = driver.find_element_by_id('tweet-box-reply-to-1043487984841048064')
    if randomornot.lower() == 'y':
        reply_box.send_keys(select_word(read_words(filename)))
        print('Sent ' + read_words(filename[i]))
    elif randomornot.lower() == 'n':
        j += 1
        reply_box.send_keys(read_words(filename)[j])
        print('Sent ' + read_words(filename[j]))

    sleep(.3)
    reply_box.send_keys(Keys.CONTROL + Keys.ENTER)
    print('Outputted ', i, 'words this session')


