import pytest
# fixture method

#if scope is added as class then pre condition will run befor class methods and post conditions will run after class methods.
@pytest.fixture()
def setup():
    print("Precondition statement") 
    yield
    print("Postcondition")

@pytest.fixture()
def dataload():
    print("Data generation...")
    return ["Testing", "using", "fixtures"]
