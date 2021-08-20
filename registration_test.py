import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_new_user_registration():
    driver.get("http://localhost/litecart/")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='default-menu']/ul[2]/li/a").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="box-create-account"]/form/div[2]/div[1]/input').send_keys("Vladimir")   #name
    driver.find_element_by_xpath('//*[@id="box-create-account"]/form/div[2]/div[2]/input').send_keys("Shalnev")    #family name
    driver.find_element_by_css_selector('div.select-wrapper [name="country_code"]').click()  # Clicking at a text-box
    driver.find_element_by_xpath("//option[.='United States']").click()                      # choosing country
    driver.find_element_by_css_selector('div.select-wrapper [name="zone_code"]').click()     # clicking at a text-box
    driver.find_element_by_xpath("//option[.='Florida']").click()                            # choosing state
    driver.find_element_by_xpath('//input[@name="postcode"]').send_keys("32118")             # postal code
    driver.find_element_by_xpath('//*[@id="box-create-account"]//*[@name="email"]').send_keys("karamba@karamba.co.uk")
    driver.find_element_by_xpath('//*[@id="box-create-account"]//*[@name="password"]').send_keys(
        "shalompopolam")   # this is password
    driver.find_element_by_xpath('//*[@id="box-create-account"]//*[@name="confirmed_password"]').send_keys(
        "shalompopolam")   # confirmation of the password
    driver.find_element_by_xpath('//button[@name="create_account"]').click()   # clicking on button to create an account
    driver.find_element_by_css_selector('.account.dropdown').click()          # click to get dropdown menu before logout
    driver.find_element_by_xpath(
        '//*[@id="default-menu"]//a[@href="http://localhost/litecart/logout"]').click()  # logout
    driver.find_element_by_css_selector('.account.dropdown').click()  # click to get dropdown menu before sign in
    driver.find_element_by_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[1]/form/div[1]/div/input').clear()
    driver.find_element_by_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[1]/form/div[1]/div/input').send_keys(
        'karamba@karamba.co.uk')
    driver.find_element_by_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[1]/form/div[2]/div/input').clear()
    driver.find_element_by_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[1]/form/div[2]/div/input').send_keys(
        'shalompopolam')
    driver.find_element_by_xpath('//*[@id="default-menu"]/ul[2]/li/ul/li[1]/form/div[3]/button').click()
    driver.find_element_by_css_selector('.account.dropdown').click()  # click to get dropdown menu before logout
    driver.find_element_by_xpath(
        '//*[@id="default-menu"]//a[@href="http://localhost/litecart/logout"]').click()  # logout




