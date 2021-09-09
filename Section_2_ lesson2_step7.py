import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element_by_name("firstname").send_keys("Vadim")

    l_name = browser.find_element_by_name("lastname").send_keys("Black")

    email = browser.find_element_by_name("email").send_keys("example@mail.com")

    # получаем путь к директории текущего исполняемого скрипта Section_2_lesson2_step_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # Находим кнопку "Выбрать файл"
    element = browser.find_element_by_css_selector("[type='file']")
    # отправляем файл
    element.send_keys(file_path)

    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()