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
    driver.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(2)
    block = driver.find_element_by_xpath("//*[@id='box-apps-menu']")
    all_tabs = block.find_elements_by_css_selector("#box-apps-menu-wrapper a")

    for tab in all_tabs:
        tab.click()
        # links = all_tabs.find_elements_by_xpath('.//a')
        # driver.find_elements_by_css_selector("#box-apps-menu-wrapper a")
        # tab.click()
        # tab = driver.findElements(By.cssSelector("#box-apps-menu a"))
        # elementList.get(i).click();
        # tab.click()
        # time.sleep(1)

    # for i in range(len(all_tabs)):
    #     all_tabs[i].click()
    #     time.sleep(1)
