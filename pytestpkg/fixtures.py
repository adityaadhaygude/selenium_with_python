import pytest

#Here yield is used to calculate/execute the main functionality and then come back to the tear down statements
#before yield statements are executed then control will go to main function and after completing execution of main function control will go back to after yield statements.

@pytest.fixture()
def setup():
    print("Pre-requisite setup is done")
    yield
    print("Post execution clean up is done!")

def test_fun(setup):
    print("Actual test case is running...")