from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DriverExtensions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def navigate_to(self, url):
        """
        Navigate to a specific URL.

        Usage:
        driver_extensions.navigate_to("https://example.com")
        """
        self.driver.get(url)

    def refresh_page(self):
        """
        Refresh the current page.

        Usage:
        driver_extensions.refresh_page()
        """
        try:
            self.driver.refresh()
        except:
            self.driver.refresh()

    def back(self):
        """
        Navigate back to the previous page.

        Usage:
        driver_extensions.back()
        """
        self.driver.back()

    def get_current_url(self):
        """
        Get the current URL.

        Usage:
        current_url = driver_extensions.get_current_url()
        """
        return self.driver.current_url

    def get_page_title(self):
        """
        Get the title of the current page.

        Usage:
        page_title = driver_extensions.get_page_title()
        """
        return self.driver.title.strip()

    def take_screenshot(self, filepath):
        """
        Take a screenshot and save it to a file.

        Usage:
        driver_extensions.take_screenshot("path/to/screenshot.png")
        """
        ss_driver = self.driver
        screenshot = ss_driver.get_screenshot_as_file(filepath)

    def switch_to_iframe(self, element):
        """
        Switch to an iframe using the provided WebElement.

        Usage:
        driver_extensions.switch_to_iframe(some_element)
        """
        self.driver.switch_to.frame(element)

    def switch_to_default_iframe(self):
        """
        Switch back to the default content.

        Usage:
        driver_extensions.switch_to_default_iframe()
        """
        self.driver.switch_to.default_content()

    def accept_alert(self):
        """
        Accept the current alert.

        Usage:
        driver_extensions.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def select_window_by_title(self, title):
        """
        Switch to a window with the given title.

        Usage:
        driver_extensions.select_window_by_title("Some Window Title")
        """
        for handle in self.driver.window_handles:
            if self.driver.switch_to.window(handle).title == title:
                break

    def switch_to_last_window(self):
        """
        Switch to the last opened window.

        Usage:
        driver_extensions.switch_to_last_window()
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_first_window(self):
        """
        Switch to the first opened window.

        Usage:
        driver_extensions.switch_to_first_window()
        """
        self.driver.switch_to.window(self.driver.window_handles[0])

    def select_window_by_index(self, index):
        """
        Switch to a window using its index.

        Usage:
        driver_extensions.select_window_by_index(1)
        """
        self.driver.switch_to.window(self.driver.window_handles[index])
