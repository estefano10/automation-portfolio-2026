import sys

def test_environment():
    version = sys.version_info

    assert version >= (3, 12) , "Python version must be 3.12 or higher."
