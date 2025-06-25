import  pytest
import tempfile

@pytest.fixture
def fixture_test():
    """ Create a temporary file for testing """
    with tempfile.NamedTemporaryFile() as file:
        yield file.name


def testing_fixture_test(fixture_test):
     '''Test case '''
     with open(fixture_test, 'w') as fil:
         fil.write("Hello World")
     with open(fixture_test) as fils:
        assert fils.read() == "Hello World"