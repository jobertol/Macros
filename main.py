from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import datetime

from gpiozero import Button
from time import sleep


def logData():
  driver = webdriver.Chrome('./chromedriver')
  driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=MhlcNIFE0UypZ7uOyCLuL2gu9sul5k1IiROfNLPyDS5UQk5QRDE0SUZPM1pUM0M1NVZHNFVXMFdZRy4u&qrcode=true")
  dateBox = driver.find_element_by_class_name("office-form-question-textbox form-control border-no-radius datepicker")
  date = now().strftime("%-m/%-d/%Y")
  dateBox.send_keys(date)
  nameBox = driver.find_element_by_class_name("office-form-question-textbox office-form-textfield-input form-control border-no-radius")
  nameBox.send_keys("Joberto Lee")
  driver.find_element_by_xpath("//form[@aria-labelledby='question3-title question3-required question3-questiontype']/div[5]/input[1]").click()
  driver.find_element_by_xpath("//form[@aria-labelledby='question4-title question4-required question4-questiontype']/div[2]/input[1]").click()
  driver.find_element_by_xpath("//form[@aria-labelledby='question7-title question7-required question7-questiontype']/div[2]/input[1]").click()
  driver.find_element_by_xpath("//form[@aria-labelledby='question8-title question8-required question8-questiontype']/div[1]/input[1]").click()
  driver.find_element_by_class_name("__submit-button__ office-form-bottom-button office-form-theme-button button-control light-background-button").click()
  driver.close()



button = Button(2)

while True:
    if button.is_pressed:
        logData()
    sleep(5000)
    
    

    
    

  
