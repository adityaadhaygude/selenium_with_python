import pytest

@pytest.fixture()
def setup():
    print("Pre-requisite setup")
    yield
    print("Post test execution")