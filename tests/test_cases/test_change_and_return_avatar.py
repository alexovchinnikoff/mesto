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

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))

# В переменную old_avatar_url сохрани ссылку на изображение
old_avatar_url = 'https://pictures.s3.yandex.net/resources/jacques-cousteau_1604399756.png'

# Кликни по изображению профиля
driver.find_element(By.CLASS_NAME,"profile__image").click()

# В поле ссылки на изображение введи ссылку, используй переменную avatar_url
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(By.ID,"owner-avatar").send_keys(avatar_url)

# Сохрани новое изображение
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']").click()

# Обнови страницу
driver.refresh()

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(By.CLASS_NAME,"profile__image").get_attribute('style')

# Проверь, что в style содержится ссылка на аватар
assert avatar_url in style

# Верни старое изображение профиля
# Кликни по изображению профиля
driver.find_element(By.CLASS_NAME,"profile__image").click()

# В поле ссылки на изображение введи ссылку, используй переменную old_avatar_url
driver.find_element(By.ID, "owner-avatar").send_keys(old_avatar_url)
# Сохрани старое изображение
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']").click()
# Обнови страницу
driver.refresh()

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(By.CLASS_NAME,"profile__image").get_attribute('style')
# Проверь, что в style содержится ссылка на старый аватар
assert old_avatar_url in style

# Закрой браузер
driver.quit()
