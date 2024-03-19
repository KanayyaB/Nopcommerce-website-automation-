import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_html_report_title(report):
    report.title = "Login of NOP Commerce website"

def pytest_configure(config):
    config.stash[metadata_key]["Project_name"] = "Nop commerce"
    config.stash[metadata_key]["module_name"] = "customers"
    config.stash[metadata_key]["Tester"] = "kanayya"

