#!python3
#This program allows you to play 5 games of 2048 automatically

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\seledrivers\chromedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
elem = browser.find_element_by_tag_name('html')
scoreelem = browser.find_element_by_class_name('score-container')
numofgames = 0
scores = []

while True:
    try:
        retry = browser.find_element_by_class_name('retry-button')
        if retry.is_displayed() == True:
            scores.append(scoreelem.text)
            numofgames += 1
            print('Score of game %s is: ' %(numofgames) + scoreelem.text)
            retry.click()
    except:
        continue
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)
    if numofgames == 5:
        break

browser.quit()
print('You have played %s games automatically. Your scores have been saved:' %(numofgames))
print(scores)
scorelist = ', '.join(scores)

savedscores = open('2048_Scores.txt', 'a')
savedscores.write('\n')
savedscores.write(scorelist)
savedscores.close()
