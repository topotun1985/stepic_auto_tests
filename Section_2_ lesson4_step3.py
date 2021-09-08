from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait1.html"

try:
     browser = webdriver.Chrome()
     # говорим WebDriver искать каждый элемент в течение 5 секунд, чтобы каждый раз не использовать time.sleep
     browser.implicitly_wait(5)
     browser.get(link)

     button = browser.find_element_by_id("verify").click()
     message = browser.find_element_by_id("verify_message")

     assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()