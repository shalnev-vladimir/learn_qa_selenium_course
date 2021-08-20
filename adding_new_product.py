import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_searching_for_elements_in_admin_menu(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".btn.btn-default").click()     # now we are in admin cabinet
    time.sleep(2)
    driver.find_element_by_css_selector("#app-catalog > a").click()     # click on catalog button
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/ul/li[3]/a').click()  # click on Add New Product button
    time.sleep(2)
    driver.find_element_by_css_selector('label.btn.btn-default:first-child').click()  # switching to enable
    time.sleep(2)                                                        # Enter the name of the new product
    driver.find_element_by_xpath('//input[@name="name[en]"]').send_keys('It is definitely brand new product!!!')
    time.sleep(2)
    driver.find_element_by_xpath('//input[@type="checkbox" and @value="1-3"]').click()
    driver.find_element_by_xpath('//input[@name="code"]').send_keys('777')
    # mouse left click to open drop down menu "Manufacturer"
    driver.find_element_by_xpath('//select[@name="manufacturer_id"]').click()
    # choosing the second menu item
    driver.find_element_by_xpath('//option[.="ACME Corp."]').click()
    time.sleep(2)
    # looking for supplier id drop down menu
    driver.find_element_by_xpath('//select[@name="supplier_id"]').click()
    # input keywords
    driver.find_element_by_name('keywords').send_keys('owls')
    # we'll have Date Valid From here
    driver.find_element_by_name('date_valid_from').send_keys('21092021')
    # and Date Valid To, too
    driver.find_element_by_name('date_valid_to').send_keys("21122021")
    # adding of the product
    # driver.find_element_by_xpath('//input[@type="file"]').click()
    # click Save
    driver.find_element_by_xpath('//button[@name="save"]').click()
    time.sleep(3)
    # choosing the tab Information
    driver.find_element_by_xpath('//a[@href="#tab-information"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@name="short_description[en]"]').send_keys("The best thing you've ever seen!")
    driver.find_element_by_xpath('//div[@class="trumbowyg-editor trumbowyg-autogrow-on-enter"]').send_keys('This is '
                                                                                                           'what you '
                                                                                                           'wanna '
                                                                                                           'have!!')
    time.sleep(3)
    driver.find_element_by_xpath('//textarea[@name="attributes[en]"]').send_keys("Here you'll find some Attributes. "
                                                                                 "Actually, I have no idea what does "
                                                                                 "it mean)")
    driver.find_element_by_xpath('//input[@name="head_title[en]"]').send_keys('Hi there!!')
    driver.find_element_by_xpath('//input[@name="meta_description[en]"]').send_keys('What is those?!)')
    time.sleep(1)
    driver.find_element_by_xpath('//button[@name="save"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//a[@href="#tab-prices"]').click()
    time.sleep(3)
    driver.find_element_by_css_selector('input[name="purchase_price"]').clear()        # Purchase Price
    driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys("1,000,000")
    driver.find_element_by_css_selector('select[name="purchase_price_currency_code"]').click()      # currency
    driver.find_element_by_xpath('//option[@value="USD"]').click()                        # choose USD
    time.sleep(1)
    driver.find_element_by_name('gross_prices[USD]').send_keys('5')    # filling Price Incl. Tax box
    time.sleep(3)
    driver.find_element_by_xpath('//button[@value="Save"]').click()
