import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
import time
from  Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_login:
    BaseURl = Readconfig.getApplicationURl()
    path=r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\TestData\LoginData.xlsx"
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.log.info("--------Test_002_DDT_login--------------")
        self.log.info("-----------login DDT Test-----------")
        screenshot_path = r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Screenshots\screenshot9.png"
        self.driver = setup
        self.driver.get(self.BaseURl)
        lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet2')
        self.log.info(self.rows)
        print("number of rows in excel", self.rows)

        list_status=[]   # empty list varible
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet2',r,1)
            self.pas =  XLUtils.readData(self.path,'Sheet2',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet2', r, 3)
            time.sleep(2)
            lp.setUsername(self.user)
            time.sleep(2)
            lp.setPassword(self.pas)
            time.sleep(2)
            self.log.info("-----------click on submit button-----------")
            lp.clickLogin()
            act_title = self.driver.title
            exp_title ="Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("*****Passed")
                    time.sleep(2)
                    lp.logout()
                    time.sleep(2)
                    list_status.append("Pass")
                elif self.exp =="Fail":
                    self.log.info("*****Failed")
                    lp.logout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.log.info("*****Failed")
                    list_status.append("Fail")
                elif self.exp =="Fail":
                    self.log.info("*****Passed")
                    list_status.append("Pass")

        self.log.info(list_status)

        if "Fail" not in list_status:
            self.log.info("********Login DDT test passed*****")
            self.driver.close()
            assert True
        else:
            self.log.info("********Login DDT test Failed*****")
            self.driver.close()
            assert False

        self.log.info("-----------End of Login DDT Test-----------")
        self.log.info("-----------Completed Test_002_DDT_login-----------")
