import os
from webdriver_manager.chrome import ChromeDriverManager
from dash.testing.application_runners import import_app

# Download chromedriver and add its directory to PATH
chromedriver_path = ChromeDriverManager().install()
os.environ["PATH"] = os.path.dirname(chromedriver_path) + os.pathsep + os.environ["PATH"]

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
