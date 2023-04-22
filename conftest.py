from selenium import webdriver
import pytest


@pytest.fixture()  # Таким образом функция будет восприниматься, как фикстура
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
