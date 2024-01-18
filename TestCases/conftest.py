import configparser

from  selenium import webdriver
import pytest
config = configparser.RawConfigParser()
config.read(r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Configurations\config.ini")


@pytest.fixture()
def setup():
    browsername = config.get('common', 'browser')

    if browsername == 'chrome':
        driver = webdriver.Chrome()
    elif browsername == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver


# """PyTest HTML Report"""
# def pytest_configure(config):
#     config.metadata['Project Name'] = "Sample project"
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins",None)

# def pytest_addoption(parser):
#     parser.addoption("--browser--")


# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
