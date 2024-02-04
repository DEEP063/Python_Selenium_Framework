from selenium import webdriver

import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# Fixture to capture screenshots on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        # If the test failed, capture a screenshot
        driver = item.cls.driver  # Assuming your driver is stored in the 'driver' attribute of the test class
        screenshot_path = f"Screenshots/{item.name}_failure.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
