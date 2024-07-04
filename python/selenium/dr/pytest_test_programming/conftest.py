import pytest

# we can use scope also like @pytest.fixture(autouse=True,scope="session") # this autouse-true,scope="session" will make it(setup) run once before running all test method in the directory and then towards the end it will run teardown code.
@pytest.fixture(autouse=True) # this autouse-true will make it(setup and teardown function) run before and after every test method in the directory.
def setup_and_teardown():
    print("open browser")
    yield
    print("close browser")