
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjects.basePO import BasePO


class SignUp_LoginPage(BasePO):
    emailTextbox = "//form[@action='/login']//input[@name='email']"
    passwordTextbox = "//form[@action='/login']//input[@name='password']"
    LoginButton = "//button[text()='Login']"

    def __init__(self, driver):
        super().__init__(driver)


    def enterEmail(self,email):
        self.wait.wait_for_element_visible(By.XPATH,self.emailTextbox).send_keys(email)

    def enterPassword(self, password):
        # self.wait.element_to_be_clickable(self.passwordTextbox).send_keys(password)
        self.wait.wait_for_element_visible(By.XPATH,self.passwordTextbox).send_keys(password)

    def clickOnLoginButton(self):
        self.wait.element_to_be_clickable_by_locator(By.XPATH,self.LoginButton).click()
