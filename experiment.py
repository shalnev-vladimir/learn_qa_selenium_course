import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


# def test_are_elements_present(driver):
#     driver.get("http://localhost/litecart/")
#     time.sleep(2)
#     driver.find_element_by_css_selector("#content > ul > li.active > a").click()
#     time.sleep(1)
#     driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
#     time.sleep(1)
#     driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
#     time.sleep(1)
#     driver.find_element_by_css_selector("#content > ul > li:nth-child(1) > a").click()
#     time.sleep(1)
#     driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
#     time.sleep(1)
#     box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(1)")
#     time.sleep(2)
#     quantity_of_stickers = box1.find_elements_by_class_name("sticker")
#     print(len(quantity_of_stickers))

def test_expects_11(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    stickers = driver.find_elements_by_class_name("sticker")
    time.sleep(1)
    print("We have ", len(stickers), " stickers. Yo!")


def test_sticker_picker(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(1) > a").click()
    time.sleep(1)
    the_only_box = driver.find_element_by_css_selector("#box-campaign-products > div > div:nth-child(1)")
    time.sleep(1)
    stickers_pickers = the_only_box.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_popular_products_box1(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-popular-products > div > div:nth-child(1)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_popular_products_box2(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-popular-products > div > div:nth-child(2)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_popular_products_box3(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-popular-products > div > div:nth-child(3)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_popular_products_box4(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-popular-products > div > div:nth-child(4)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_popular_products_box5(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-popular-products > div > div:nth-child(5)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_latest_products_box1(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(1)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_latest_products_box2(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(2)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_latest_products_box3(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(3)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_latest_products_box4(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(4)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))


def test_stickers_latest_products_box5(driver):
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
    time.sleep(1)
    box1 = driver.find_element_by_css_selector("#box-latest-products > div > div:nth-child(5)")
    time.sleep(1)
    stickers_pickers = box1.find_elements_by_class_name("sticker")
    print(len(stickers_pickers))

# def test_expects_5(driver):
#     driver.get("http://localhost/litecart/")
#     time.sleep(2)
#     driver.find_element_by_css_selector("#content > ul > li:nth-child(3) > a").click()
#     time.sleep(1)
#     boxes = driver.find_elements_by_id("div.tab-content .image")
#     time.sleep(1)
#     # stickers_pickers = boxes.find_elements_by_class_name("sticker")
#     print(len(boxes))
