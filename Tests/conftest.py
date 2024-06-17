import pytest

@pytest.fixture(scope="class")
def greeting():
    print("The Function has started.")
    yield
    print("The Function has completed.")