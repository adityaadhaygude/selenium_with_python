import pytest

@pytest.mark.usefixtures("crossBrowser")
class Test1:
    def test_crossBrowser(self, crossBrowser):
        print(crossBrowser)

    def test_crossBrowser_multioptions(self, crossBrowser):
        print(crossBrowser[1])