from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("ov4.alex@ya.ru")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//li[@class='places__item card']//h2[@class='card__title']")))

# Запомни title последней карточки
title_before = driver.find_element(By.XPATH, ".//li[@class='places__item card']//h2[@class='card__title']").text

# Кликни по кнопке добавления нового контента
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# Введи название нового места, оно должно отличаться от названия последней карточки
new_title = "Москва 18:25:36-25.11.2022"
driver.find_element(By.NAME, "name").send_keys(new_title)

# Введи ссылку на изображение
driver.find_element(By.NAME, "link").send_keys(
    "https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg")

# Сохрани контент
driver.find_element(By.XPATH, ".//form[@name='new-card']/button[text()='Сохранить']").click()

# Дождись, пока появится кнопка удаления карточки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, ".//button[@class='card__delete-button card__delete-button_visible']")))

# Проверь, что на карточке отображается верное название
title_after = driver.find_element(By.XPATH, ".//li[@class='places__item card']//h2[@class='card__title']")
assert title_after.text == new_title