import pytest
from selene import browser

browser.config.base_url = "https://google.com"


@pytest.fixture(scope="function")
def browser_size():
    browser.config.window_width = 80
    browser.config.window_height = 80
