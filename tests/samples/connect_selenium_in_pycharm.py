from selenium import webdriver
#import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions() # создаешь объект для опций
chrome_options.add_argument('--headless') # добавляешь настройку
chrome_options.add_argument('--window-size=640,480') # добавляешь ещё настройку
driver = webdriver.Chrome(options=chrome_options) # создаешь драйвер и передаешь в него настройки 
driver.maximize_window() # полноэкранный режим

driver.get('https://qa-mesto.praktikum-services.ru/')

assert '/signin' in driver.current_url

# закроем браузер
driver.quit()
