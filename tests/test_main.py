import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Поиск товара и ожидание появления одного товара
def test_main_page_1(browser, url):
    browser.get(url)
    text = browser.find_element(By.CSS_SELECTOR, ".input-lg")
    text.click()
    text.send_keys("Iphone")
    browser.find_element(By.CSS_SELECTOR, ".btn-lg").click()
    browser.find_element(By.CSS_SELECTOR, ".product-thumb")
    card = browser.find_elements(By.CSS_SELECTOR, ".product-layout")
    assert len(card) == 1, "Количество элементов (карточек товара) больше"


# Добавление первого товара в корзину и ожидание появляения алерта.
# Чтобы выбрать другой товар, необходимо заменить число первого селектора nth-child
def test_main_page_2(browser, url):
    browser.get(url)
    button = browser.find_element(By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.button-group > "
                                                   "button:nth-child(1)")
    button_buy = ActionChains(browser)
    button_buy.move_to_element(button).perform()
    button.click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))


# Проверка наличия товара в корзине
def test_main_page_3(browser, url):
    browser.get(url)
    find_buy_button = browser.find_element(By.CSS_SELECTOR, "#content > div.row > div:nth-child(2) > div > "
                                                            "div.button-group > button:nth-child(1)")
    button_buy = ActionChains(browser)
    button_buy.move_to_element(find_buy_button).perform()
    find_buy_button.click()
    time.sleep(3)
    find_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-block.dropdown-toggle")
    find_cart_button.click()
    find_button_to_cart = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cart"
                                                                                                      "']/ul/li["
                                                                                                      "2]/div/p/a["
                                                                                                      "1]/strong")))
    find_button_to_cart.click()
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")


# Проверка работы слайдера
def test_main_page_4(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, ".text-center.swiper-slide-active > a > img").click()
    browser.find_element(By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")


# Проверка страниц авторизации и регистрации
def test_main_page_5(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#top-links>ul>li.dropdown>a>span.hidden-xs.hidden-sm.hidden-md").click()
    browser.find_element(By.CSS_SELECTOR, "#top-links>ul>li.dropdown.open>ul>li:nth-child(1)>a").click()
