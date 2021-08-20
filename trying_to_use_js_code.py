import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_by_js(driver):
    driver.get("http://localhost/litecart/admin/")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#app-countries > a").click()
    time.sleep(2)
    array = driver.execute_script(
        "capitals = [];" +
        "table = document.querySelector('#main > form');" +
        "rows = table.querySelectorAll('tr');" +
        "for (var i = 1; i < rows.length; ++i) {" +
        "cells = rows[i].querySelectorAll('td');" +
        "capitals.push([cells[0].textContent, cells[1].textContent]);" +
        "};" +
        "return capitals;")
    print({pair[0]: pair[1] for pair in array})
