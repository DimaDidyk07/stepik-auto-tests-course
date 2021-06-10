from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_elem = browser.find_element_by_id("num1")
    num2_elem = browser.find_element_by_id("num2")
    num1 = num1_elem.text
    num2 = num2_elem.text
    Sum = str(str(int(num1)+int(num2)))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(Sum)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()