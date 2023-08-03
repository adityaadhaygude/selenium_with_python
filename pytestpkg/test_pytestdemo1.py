import pytest

#add -m tag to run the labelled test cases e.g py.test -m smoke -vs
# -v is for details and -s to print to console
# -k is used to pass partial name/regular expression to run multiples methods and files

@pytest.mark.smoke
def test_hello():
    print("Hello")

def test_travel_vlog():
    print("Welcome to my vlog!")