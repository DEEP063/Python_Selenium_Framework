import string
import time

import pytest
from selenium import webdriver
from pageObjects.homePage import HomePage
from pageObjects.SignUp_LoginPage import SignUp_LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testCases.BaseTest import BaseTest
from utilities.readProperties import ReadConfig
from utilities import XUtils

import random
import string

class Test_registerUser_excel_ddt(BaseTest):
    baseUrl = ReadConfig.getApplicationUrl()
    path = "C:\\Users\\SAI-PC\\Desktop\\pythonProject001\\TestData\\Book2.xlsx"

    def random_string(self,length):
        """
        Generate a random string of specified length.

        Args:
        length (int): The length of the random string to generate.

        Returns:
        str: A random string of the specified length.
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    @pytest.mark.regression
    def test_login_user_ex(self, setup):

        self.logger.info("*********************Started**************************")
        self.logger.info("*********************test_login_user**************************")
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.sp = SignUp_LoginPage(self.driver)

        self.hp.navigateToPage(self.baseUrl)
        time.sleep(2)
        self.hp.clickOnLink()
        time.sleep(3)


        print("#############################################")
        print(XUtils.getRowCount(self.path,"Sheet1"))
        self.rows = XUtils.getRowCount(self.path,"Sheet1")

        for r in range(2, self.rows + 1):
            self.email = XUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XUtils.readData(self.path, 'Sheet1', r, 2)
            self.sp.enterEmail(self.email)
            self.sp.enterPassword(self.password)
            self.sp.clickOnLoginButton()
            time.sleep(4)

        self.logger.info("*********************End**************************")
        self.logger.info("*********************TestEnd**************************")
