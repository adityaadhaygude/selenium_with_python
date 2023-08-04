import pytest

# fixture method setup declared at the class level
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_demo(self):
        print("Actual test scenario1")

    def test_demo1(self):
        print("Actual test scenario2")

