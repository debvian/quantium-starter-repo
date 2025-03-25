import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to start the app
@pytest.fixture
def dash_app():
    app = import_app("app")  # Import your Dash app
    return app

@pytest.fixture
def dash_duo(dash_thread_server):
    """Set up Dash test runner with proper Chrome WebDriver"""
    service = Service(ChromeDriverManager().install())  # Auto-download Chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run tests in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)

    with dash_thread_server(driver) as server:
        yield server

# Test 1: Check if the **Header** is present
def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    WebDriverWait(dash_duo.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Dashboard"

# Test 2: Check if the **Graph** is present
def test_graph_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    WebDriverWait(dash_duo.driver, 10).until(EC.presence_of_element_located((By.ID, "sales-line-chart")))
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# Test 3: Check if the **Region Picker** (Radio Buttons) is present
def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    WebDriverWait(dash_duo.driver, 10).until(EC.presence_of_element_located((By.ID, "region-filter")))
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
