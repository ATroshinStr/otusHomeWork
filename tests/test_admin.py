import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Валидация на неверный логин или пароль
def test_admin_page_1(browser, url):
    browser.get(url + "admin")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))


# Валидация на существующий аккаунт для восстановления пароля
def test_admin_page_2(browser, url):
    browser.get(url + "admin")
    browser.find_element(By.CSS_SELECTOR, "div:nth-child(2)>span>a").click()
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))


# Проверка кнопки отмены на странице Восстановления пароля
def test_admin_page_3(browser, url):
    browser.get(url + "admin")
    browser.find_element(By.CSS_SELECTOR, "div:nth-child(2)>span>a").click()
    browser.find_element(By.CSS_SELECTOR, "div.text-right > a").click()


# Проверка вводимых символов в поле Логин
def test_admin_page_4(browser, url):
    browser.get(url + "admin")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("_#$%@_")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("_qwerty_")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("_абвгд_")


# Проверка валидации на авторизацию без заполения пароля
def test_admin_page_5(browser, url):
    browser.get(url + "admin")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
