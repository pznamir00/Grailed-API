def pytest_addoption(parser):
    parser.addoption("--x_algolia_api_key", action="store")
    parser.addoption("--x_algolia_app_id", action="store")
