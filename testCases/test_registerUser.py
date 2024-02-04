import time

import pytest
from selenium import webdriver
from pageObjects.homePage import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Test_RegisterUser:

    def test_register_a_new_user(self,setup):
        self.driver= setup
        expected_url = "5https://automationexercise.com/view_cart"

        self.hp = HomePage(self.driver)

        self.hp.navigateToPage()
        time.sleep(1)
        self.hp.clickOnTitle()
        time.sleep(1)
        self.hp.clickOnLink()
        time.sleep(2)

        actual_url = self.hp.getUrl()
        print()

        assert expected_url == actual_url,f"{actual_url} usrl is not correct"

