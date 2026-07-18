from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID,"email").send_keys("ov4.alex@ya.ru")
driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.CLASS_NAME,"auth-form__button").click()

# Добавь явное ожидание появления последней карточки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Запомни title последней карточки
title_before = driver.find_element(By.CLASS_NAME,"card__title").text

# Кликни по кнопке добавления нового контента
driver.find_element(By.CLASS_NAME,"profile__add-button").click()

# Введи название нового места, оно должно отличаться от названия последней карточки
new_title = "МоскваПочемЗвонятТвоиКолокола"
driver.find_element(By.ID,"place-name").send_keys(new_title)

# В поле ссылки на изображение введи ссылку
link = "https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg"
driver.find_element(By.ID,"place-link").send_keys(link)
# Сохрани контент
driver.find_element(By.XPATH, ".//form[@name='new-card']/button[text()='Сохранить']").click()
# Дождись появления кнопки удаления карточки
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__delete-button")))

# Проверь, что на карточке отображается верное название
title_after = driver.find_element(By.CLASS_NAME,"card__title").text
assert new_title in title_after

# Запомни количество карточек до удаления
cards_before = len(driver.find_elements(By.CLASS_NAME, "places__item"))

# Удали карточку
driver.find_element(By.CLASS_NAME, "card__delete-button").click()
# Дождись, что title последней карточки равен title_before
driver.refresh()
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__title")))
title_after = driver.find_element(By.CLASS_NAME,"card__title").text
assert title_before in title_after
# Проверь, что количество карточек стало на одну меньше
cards_after = len(driver.find_elements(By.CLASS_NAME, "places__item"))
assert cards_after == cards_before - 1

# Закрой браузер
driver.quit()
