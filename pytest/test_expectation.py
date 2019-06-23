# content of test_expectation.py

# coding:utf-8

import pytest
@pytest.mark.parametrize("test_input,expected",
                         [ ("3+5", 8),
                           ("2+4", 6),
                           ("6 * 9", 42),
                         ])
def test_eval(test_input, expected, flag):
    assert eval(test_input) == expected

if __name__ == "__main__":
    # pytest.main(["-s", "test_expectation.py", "--html=report.html"])
    pytest.main(["-s", "test_expectation.py"])