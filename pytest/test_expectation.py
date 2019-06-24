# content of test_expectation.py

# coding:utf-8
import pytest

class Test:
    def RiskTolerance(num=None):

        def wrapper(func):
            def inner_wrapper(self, *args, **kwargs):
                print("正在执行用例 :", func.__name__)
                print(*args, **kwargs, "sssssssssssssssssssssss")
                return func(self, *args, **kwargs)
            return inner_wrapper
        return wrapper





    @RiskTolerance(num=1)
    @pytest.mark.parametrize("test_input,expected",
                             [ ("3+5", 8),
                               ("2+4", 6),
                               ("6 * 9", 42),
                             ])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected

if __name__ == "__main__":
    # pytest.main(["-s", "test_expectation.py", "--html=report.html"])
    pytest.main(["-s", "test_expectation.py"])