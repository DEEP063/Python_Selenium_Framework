
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
    # navigational_link = "//a[normalize-space()='Signup / Login']"
    url = "https://automationexercise.com/"
    title = "//img[@alt='Website for automation practice']"

    emailTextbox = "//form[@action='/login']//input[@name='email']"
    passwordTextbox = "//form[@action='/login']//input[@name='password']"
    LoginButton = "//button[text()='Login']"
    def navigational_link(self, link):
        # return f"//a[normalize-space()='{link}']"
        return f"//a[contains(@href,'{link}')]"



    def __init__(self, driver):
        super().__init__(driver)

    def getUrl(self):
        return self.driver.get_current_url()

    def navigateToPage(self,URL=url):
        self.driver.navigate_to(URL)

    def clickOnLink(self ,link='login'):
      #self.wait.element_to_be_clickable_by_locator(By.XPATH,self.navigational_link).click()
      self.wait.wait_for_element_visible(By.XPATH,self.navigational_link(link)).click()

    def clickOnTitle(self):
        self.wait.wait_for_element_visible(By.XPATH,self.title)

