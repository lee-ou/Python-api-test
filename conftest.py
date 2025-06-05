import pytest

from utils.yaml_handle import clear_extract


@pytest.fixture(scope='session', autouse=True)
def handle_fixture():
    clear_extract()
