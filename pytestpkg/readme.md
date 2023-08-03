# All test case and package file names should start with test_ or ends with _test is mandatory for the seamless execution

# basic command to run test case using pytest
    py.test 
  It will run all the test cases from the folder

# -v is for details and -s to print to console

# to run specific test case use
    py.test <filename> -vs

# add -m tag to run the labelled test cases e.g py.test -m smoke -vs

# -k is used to pass partial name/regular expression to run multiples methods and files

# pytest supports conftest.py file which should contain common setup functionality which can be reused in other test files like opening browser functionality is common. So we can declare a fixture for the same in the conftest.py file