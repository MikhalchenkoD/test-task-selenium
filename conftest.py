import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    b = webdriver.Chrome()
    yield b
    b.quit()