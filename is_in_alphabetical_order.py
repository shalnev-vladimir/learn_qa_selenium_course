import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_is_in_alphabet_order(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#app-countries > a").click()
    countries = driver.find_elements_by_css_selector("tr > td:nth-child(5) > a")
    first_letter_of_country = []
    for country in countries:
        first_letter_of_country.append(country.text[0])
    if first_letter_of_country == sorted(first_letter_of_country):
        print(' *** Всё в порядке ***')
    else:
        print(' *** С порядком тут не очень ***')
