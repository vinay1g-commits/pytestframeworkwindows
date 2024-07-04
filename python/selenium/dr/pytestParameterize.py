import pytest


@pytest.mark.parametrize("un,pswd",[("vinay","123"),("kumar","123"),("giri","123")])
def test_sampleo(un,pswd):
    print(un+"--"+pswd)

# pytest pytestParameterize.py -rA