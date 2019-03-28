#!python3
#this program uses selenium to login to BBDC and bring you to the booking page

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('C:\seledrivers\chromedriver.exe')
url = 'https://www.bbdc.sg/bbweb'
browser.get(url)
frame = browser.find_element_by_xpath("//iframe[@scrolling='no']")
browser.switch_to.frame(frame)
nricelem = browser.find_element_by_xpath("//input[@type='text'][@name='txtNRIC']")
nricelem.send_keys(#YOURUSERNAME)
passwelem = browser.find_element_by_xpath("//input[@type='password'][@name='txtPassword']")
passwelem.send_keys(#YOURPASSWORD)
loginelem = browser.find_element_by_xpath("//input[@type='submit'][@name='btnLogin']")
loginelem.click()


sideframe = browser.find_element_by_name('leftFrame')
browser.switch_to.frame(sideframe)
bookingbutt = browser.find_element_by_link_text('Booking without Fixed Instructor')
bookingbutt.click()
browser.switch_to.default_content()
mainframe = browser.find_element_by_name('mainFrame')
browser.switch_to.frame(mainframe)
agreebutt = browser.find_element_by_xpath("//input[@type='button'][@value='I Agree']")
agreebutt.click()
browser.switch_to.default_content()

time.sleep(1)
mainframe = browser.find_element_by_name('mainFrame')
browser.switch_to.frame(mainframe)
allmonths = browser.find_element_by_name('allMonth')
allmonths.click()
allsess = browser.find_element_by_name('allSes')
allsess.click()
alldays = browser.find_element_by_name('allDay')
alldays.click()
searchbutt = browser.find_element_by_xpath("//input[@type='button'][@value='Search']")
searchbutt.click()
browser.switch_to.alert.dismiss()
browser.switch_to.default_content()

mainframe = browser.find_element_by_name('mainFrame')
browser.switch_to.frame(mainframe)
allslots = find_elements_by_xpath("//input[@type='checkbox']")
for slots in allslots:
    pass
    


