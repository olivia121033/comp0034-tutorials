# Placeholder
from selenium.webdriver.chrome.options import Options
import os

def pytest_setup_options():
    options = Options()
    if "GITHUB_ACTIONS" in os.environ:
        options.add_argument("--headless")
    else:
        options.add_argument("start-maximized")

    #options.add_argument("--headless")  # Run Chrome in headless mode
    #service = Service(ChromeDriverManager().install())
    return options
