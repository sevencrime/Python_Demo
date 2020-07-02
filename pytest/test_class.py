

import pytest

gm = ""

@pytest.fixture(scope="session")
def demo():
    print("\nclass")
    global gm
    gm = "333"



@pytest.mark.usefixtures('demo')
class Test_Pytest():

    print("55555555555555555555")

    @pytest.mark.skipif(gm != "33333", reason="111111111{0}222".format(gm))
    def test_two(self):
        print("111111111111111")
        print(gm)


if __name__ == "__main__":
    pytest.main(["-v", "-s","test_class.py"])