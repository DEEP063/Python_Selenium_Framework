
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjects.basePO import BasePO


class HomePage(BasePO):
    #navigational_link = "//a[normalize-space()='Cart']"
    navigational_link = lambda link: (By.XPATH, f"//a[normalize-space()={link}]")
    url = "https://automationexercise.com/"
    title = "//img[@alt='Website for automation practice']"

    emailTextbox = "//form[@action='/login']//input[@name='email']"
    passwordTextbox = "//form[@action='/login']//input[@name='password']"
    LoginButton = "//button[text()='Login']"

    def __init__(self, driver):
        super().__init__(driver)

    def getUrl(self):
        return self.driver.get_current_url()

    def navigateToPage(self,URL  = self.url):
        self.driver.navigate_to(URL)

    def clickOnLink(self,link = 'Signup/Login'):
       self.wait.element_to_be_clickable(By.XPATH,self.navigational_link(link)).click()

    def clickOnTitle(self):
        self.wait.wait_for_element_visible(By.XPATH,self.title)

    def enterEmail(self,email):
        self.wait.element_to_be_clickable(self.emailTextbox).send_keys(email)

    def enterPassword(self, password):
        self.wait.element_to_be_clickable(self.passwordTextbox).send_keys(password)

    def clickOnLoginButton(self):
        self.wait.element_to_be_clickable(self.LoginButton).click()