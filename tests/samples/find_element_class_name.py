from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# найди заголовок
driver.find_element(By.CLASS_NAME, "auth-form__title")
# Закрой браузер
driver.quit()
