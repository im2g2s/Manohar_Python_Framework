import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    # lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//ul[@class='nav nav-treeview']//p[text()=' Customers']"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver =driver

    def clickOnCustomersMenu(self):
         WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lnkCustomers_menu_xpath))).click()

    def clickOnCustomersMenuItem(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lnkCustomers_menuitem_xpath))).click()

    def clickOnAddnew(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.btnAddnew_xpath))).click()

    def setEmail(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtEmail_xpath))).send_keys(email)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtPassword_xpath))).send_keys(password)

    def setCustomerRoles(self, role):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtcustomerRoles_xpath))).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemRegistered_xpath)))
        elif role == 'Administrators':
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemAdministrators_xpath)))
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"))).click()
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemGuests_xpath)))
        elif role == 'Registered':
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemRegistered_xpath)))
        elif role == 'Vendors':
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemVendors_xpath)))
        else:
            self.listitem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.lstitemGuests_xpath)))
        time.sleep(3)
        # self.listitem.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.listitem))).click()
        # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.drpmgrOfVendor_xpath))))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,self.rdMaleGender_id))).click()
        elif gender == 'Female':
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,self.rdFeMaleGender_id))).click()
        else:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,self.rdMaleGender_id))).click()

    def setFirstName(self, fname):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtFirstName_xpath))).send_keys(fname)

    def setLastName(self, lname):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtLastName_xpath))).send_keys(lname)

    def setDob(self, dob):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtDob_xpath))).send_keys(dob)

    def setCompanyName(self, comname):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtCompanyName_xpath))).send_keys(comname)

    def setAdminContent(self, content):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.txtAdminContent_xpath))).send_keys(content)

    def clickOnSave(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.btnSave_xpath))).click()