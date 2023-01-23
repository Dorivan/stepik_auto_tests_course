import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox(executable_path='C:/geckodriver/geckodriver.exe')

driver.get("https://stepik.org/lesson/25969/step/8")