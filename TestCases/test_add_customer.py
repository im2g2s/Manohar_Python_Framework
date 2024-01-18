
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from Utilities.readProperties import Readconfig
import time
from  Utilities.customLogger import LogGen
from Utilities import XLUtils
import pytest
import time
from PageObjects.AddNewCustomerPage import AddCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    BaseURl = Readconfig.getApplicationURl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger  = LogGen.loggen()


    # def generate_random_string(length=8):
    #     characters = string.ascii_letters + string.digits
    #     return ''.join(random.choice(characters) for _ in range(length))

    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.BaseURl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("************* Providing customer info **********")
        # time.sleep(10)
        self.addcust.setPassword("test123")
        # time.sleep(10)
        # self.email = self.generate_random_string() + "@gmail.com"
        self.email = "shamerkud@gmail.com"
        self.addcust.setEmail(self.email)
        time.sleep(10)

        self.addcust.setPassword("test123")
        # self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()
        time.sleep(2)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        # self.msg = self.driver.find_element_by_tag_name("body").text
        # self.message = self.driver.find_element(By.XPATH,"from selenium.webdriver.common.by import By").text
        #
        # print(self.message)
        # if 'customer has been added successfully.' in self.message:
        #     assert True
        #     self.logger.info("********* Add customer Test Passed *********")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
        #     self.logger.error("********* Add customer Test Failed ************")
        #     assert False


        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


