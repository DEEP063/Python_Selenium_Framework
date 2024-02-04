
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
    navigational_link = "//a[normalize-space()='Cart']"
    url = "https://automationexercise.com/"
    title = "//img[@alt='Website for automation practice']"

    def __init__(self, driver):
        super().__init__(driver)

    def getUrl(self):
        return self.driver.get_current_url()

    def navigateToPage(self):
        self.driver.navigate_to(self.url)

    def clickOnLink(self):
       self.wait.wait_for_element_visible(By.XPATH,self.navigational_link).click()

    def clickOnTitle(self):
        self.wait.wait_for_element_visible(By.XPATH,self.title)

