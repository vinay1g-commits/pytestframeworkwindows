import pytest


@pytest.mark.smoke
def test_sampleE():
    a=5
    b=6
    assert (a+b).__eq__("11")