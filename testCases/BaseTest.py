from selenium import webdriver

import pytest

import pytest
from selenium import webdriver
import os



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
