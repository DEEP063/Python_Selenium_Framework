import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.homePage import HomePage
from pageObjects.SignUp_LoginPage import SignUp_LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testCases.BaseTest import BaseTest
from utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_RegisterUser(BaseTest):
    baseUrl = ReadConfig.getApplicationUrl()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_register_a_new_user(self,setup):
        self.driver= setup
        self.hp = HomePage(self.driver)
        self.hp.navigateToPage(self.baseUrl)
        time.sleep(1)
        self.hp.clickOnTitle()
        time.sleep(1)
        self.hp.clickOnLink('products')
        time.sleep(2)

        actual_url = self.hp.getUrl()
        print()
        expected_url = "https://automationexercise.com/login"
        # assert expected_url == actual_url,f"{actual_url} url is not correct"
        if(expected_url != actual_url):
            allure.attach(self.driver.get_screenshot_as_png(),name="abcd",attachment_type=AttachmentType.PNG)
            assert False

    def test_login_user_only(self, setup):

        self.logger.info("*********************Started**************************")
        self.logger.info("*********************test_login_user**************************")
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.sp = SignUp_LoginPage(self.driver)

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.hp.navigateToPage(self.baseUrl)
        time.sleep(2)
        self.hp.clickOnLink()
        time.sleep(3)
        self.sp.enterEmail(self.email)
        self.sp.enterPassword(self.password)
        self.sp.clickOnLoginButton()
        time.sleep(4)

        self.logger.info("*********************End**************************")
        self.logger.info("*********************TestEnd**************************")
