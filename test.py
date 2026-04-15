import pytest
from app import app
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods" in header.text

def test_chart_present(dash_duo):
    dash_duo.start_server(app)
    chart = dash_duo.find_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None