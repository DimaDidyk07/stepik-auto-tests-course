from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()

    browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button1 = browser.find_element_by_id("book")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    test_input = browser.find_element_by_id("answer")
    test_input.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

