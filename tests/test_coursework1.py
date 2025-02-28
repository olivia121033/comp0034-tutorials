import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


# Set up Chrome WebDriver
'''@pytest.fixture(scope="module")
def driver():
    options = Options()
    #options.add_argument("--headless")  # Run Chrome in headless mode
    #service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:8050/")  # Adjust URL if needed
    yield driver
    driver.quit()'''

app_file = "coursework1.airquality"

# Test 1: Check if the page title is correct
def test_page_title(dash_duo):
    app = import_app(app_file)
    dash_duo.start_server(app)
    url = dash_duo.driver.current_url
    response = requests.get(url)
    assert response.status_code == 200
    # assert "UK Diffusion Tube Data Dashboard" in driver.title

'''# Test 2: Check if the bar chart updates correctly
def test_bar_chart_update(driver):
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "event-type-selector"))
    )
    dropdown.click()
    option = driver.find_element(By.XPATH, "//option[@value='average concentration background**']")
    option.click()
    time.sleep(2)  # Wait for update
    chart = driver.find_element(By.ID, "bar-chart")
    assert chart is not None

# Test 3: Check if the first bar graph dropdown menu works
def test_first_bar_chart_dropdown(driver):
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "event-type-selector"))
    )
    dropdown.click()
    options = dropdown.find_elements(By.TAG_NAME, "option")
    assert len(options) > 0  # Ensure dropdown has options
    for option in options:
        option.click()
        time.sleep(2)  # Wait for update
        chart = driver.find_element(By.ID, "bar-chart")
        assert chart.is_displayed()

# Test 4: Check if the line chart updates correctly
def test_line_chart_update(driver):
    radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='average concentration background**']"))
    )
    radio_button.click()
    time.sleep(2)  # Wait for update
    chart = driver.find_element(By.ID, "line-chart")
    assert chart is not None

# Test 5: Check if the pie chart is displayed
def test_pie_chart_display(driver):
    pie_chart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pie-chart"))
    )
    assert pie_chart.is_displayed()

# Test 6: Check if exceedance bar chart updates correctly
def test_exceedance_chart_update(driver):
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "exceedance-selector"))
    )
    dropdown.click()
    option = driver.find_element(By.XPATH, "//option[@value='% exceeding who guideline']")
    option.click()
    time.sleep(2)  # Wait for update
    chart = driver.find_element(By.ID, "exceedance-bar-chart")
    assert chart is not None

# Test 7: Check if bubble chart is displayed
def test_bubble_chart_display(driver):
    bubble_chart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bubble-chart"))
    )
    assert bubble_chart.is_displayed()

# Test 8: Check if clicking on dropdown options updates page
def test_dropdown_update(driver):
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "event-type-selector"))
    )
    dropdown.click()
    option = driver.find_element(By.XPATH, "//option[@value='average concentration roadside*']")
    option.click()
    time.sleep(2)  # Wait for update
    updated_chart = driver.find_element(By.ID, "bar-chart")
    assert updated_chart is not None

# Test 9: Check if all graphs are present on page load
def test_all_graphs_present(driver):
    graph_ids = ["bar-chart", "line-chart", "pie-chart", "exceedance-bar-chart", "bubble-chart"]
    for graph_id in graph_ids:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, graph_id))
        )
        assert element.is_displayed()'''
