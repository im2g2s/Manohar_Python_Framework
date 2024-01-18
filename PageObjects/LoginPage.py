from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_userName_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        username_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_userName_id)))
        username_textbox.clear()
        username_textbox.send_keys(username)

    def setPassword(self, password):
        password_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_password_id)))

        # Clear the password textbox
        password_textbox.clear()
        password_textbox.send_keys(password)

    def clickLogin(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.button_login_xpath)))

        btn.click()

    def logout(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath)))
        el.click()
