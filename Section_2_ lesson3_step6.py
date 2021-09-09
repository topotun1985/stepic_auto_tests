from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface").click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()