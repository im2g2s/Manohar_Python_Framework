import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
import time
from  Utilities.customLogger import LogGen

class Test_001_login:
    BaseURl = Readconfig.getApplicationURl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.log.info("********Test_001_login*************")
        self.log.info("-----------Verifying Home page-----------")
        screenshot_path = r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Screenshots\screenshot3.png"
        self.driver = setup
        self.driver.get(self.BaseURl)
        actual_title = self.driver.title


        if actual_title == "Your store. Login":
            assert True
            self.driver.save_screenshot(screenshot_path)

        else:
            self.driver.save_screenshot(screenshot_path)
            assert False

        self.log.info("-----------close-----------")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.log.info("-----------login to home page-----------")
        screenshot_path = r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Screenshots\screenshot1.png"
        self.driver = setup
        self.driver.get(self.BaseURl)
        lp = LoginPage(self.driver)
        time.sleep(2)
        lp.setUsername(self.username)
        time.sleep(2)
        lp.setPassword(self.password)
        time.sleep(2)
        self.log.info("-----------click on submit button-----------")
        lp.clickLogin()
        self.driver.save_screenshot(screenshot_path)
        self.log.info("-----------application logout-----------")
        lp.logout()
        time.sleep(5)
