import pytest

@pytest.mark.usefixtures("dataload")
class Test1:
    def test_fixture(self, dataload):
        print(dataload[0] +" "+ dataload[1] +" "+ dataload[2])