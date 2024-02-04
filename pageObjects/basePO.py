from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utilities.DriverExtensions import DriverExtensions
from utilities.waitUtils import waitUtils

class BasePO:

    def __init__(self, driver, timeout=10):
        # self.driver = driver
        self.timeout = timeout
        self.wait = waitUtils(driver)
        self.driver = DriverExtensions(driver)