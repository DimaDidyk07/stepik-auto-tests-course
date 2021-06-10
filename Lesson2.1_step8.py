from selenium import webdriver
import time
import math

def calc(x_element_valuex):
  return str(math.log(abs(12*math.sin(int(x_element_valuex)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x_element_valuex = x_element.get_attribute("valuex")
    print("Value of x:", x_element_valuex)
    y = calc(x_element_valuex)
    test_input = browser.find_element_by_id("answer")
    test_input.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()