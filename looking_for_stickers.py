import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


# def test_searching_for_elements_in_admin_menu(driver):
#     driver.get("http://localhost/litecart/")
#     time.sleep(2)
# driver.find_element_by_name("username").send_keys("admin")
# driver.find_element_by_name("password").send_keys("admin")
# tab1 = driver.find_element_by_css_selector(".active > a").click()
# product_card = tab1.find_element_by_css_selector("")
# driver.find_element_by_css_selector(".btn.btn-default").click()
# product_card = tab1.find_element_by_css_selector("#box-campaign-products a")
# stickers = product_card.find_elements_by_css_selector(".sticker")
# for sticker in stickers:

def test_are_elements_present(driver, *stickers):
    # driver.get("http://localhost/litecart/")
    # time.sleep(2)
    # tab1 = driver.find_element_by_css_selector(".active > a").click()
    # product_card = tab1.find_element_by_css_selector("#box-campaign-products a")
    # stickers = product_card.find_elements_by_css_selector(".sticker")
    return len(driver.find_elements(*stickers)) > 0


driver.get("http://localhost/litecart/")
time.sleep(2)
tab1 = driver.find_element_by_css_selector(".active > a").click()
product_card = tab1.find_element_by_css_selector("#box-campaign-products a")
stickers = product_card.find_elements_by_css_selector(".sticker")
test_are_elements_present(driver, By.CSS_SELECTOR, ".sticker")

# By.name
