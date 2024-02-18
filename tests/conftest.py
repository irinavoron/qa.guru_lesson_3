import pytest
from selene import browser

browser.config.base_url = "https://google.com"


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.window_width = 800
    browser.config.window_height = 800
    yield
    browser.quit()
