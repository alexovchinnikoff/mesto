from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди все элементы
elements = driver.find_elements(By.XPATH, ".//img")
print(len(elements))
# Проверь, что количество найденных элементов больше одного. Для этого используй функцию len()
assert len(elements) > 1

# Закрой браузер
driver.quit()
