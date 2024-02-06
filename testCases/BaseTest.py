from selenium import webdriver

import pytest

import pytest
from selenium import webdriver
import os

from utilities.customLogger import LogGen

class BaseTest:
    logger = LogGen.loggen()
