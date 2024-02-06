from selenium import webdriver

import pytest

import pytest
from selenium import webdriver
import os


@pytest.fixture()
def setup(browser):
    browser_mapping = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }

    if browser in browser_mapping:
        driver = browser_mapping[browser]()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_configure(config):
#     metadata = config.get_metadata("line")
#     metadata["Project Name"] = "Automation Exercise"
#     metadata["Module Name"] = "Register"
#     metadata["Tester"] = "Deepak"

# def pytest_configure(config):
#     config.addinivalue_line('markers', 'ProjectName: Automation Exercise')
#     config.addinivalue_line('markers', 'ModuleName: Register')
#     config.addinivalue_line('markers', 'Tester: Deepak')

def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation Exercise'
    config._metadata['Module Name'] = 'Register'
    config._metadata['Tester'] = 'Deepak'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
