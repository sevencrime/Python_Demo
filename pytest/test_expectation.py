#!/usr/bin/env/python
# -*-coding:utf-8-*-

import pytest


# 测试账号数据
test_user_data = ["admin1", "admin2"]

def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        return func(*args, **kwargs)
    return wrapper  # 返回

@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户：%s"%user)


@debug
@pytest.mark.parametrize('totalAnnual', ['小于20万', '20-50万', '50-100万', '大于100万'])
@pytest.mark.usefixtures('login')
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(totalAnnual):
    """登录用例"""

    a = login
    print("测试用例中login的返回值:%s" % a)
    print(totalAnnual)
    assert a != ""


if __name__ == "__main__":
    # pytest.main(["-s", "test_expectation.py", "--html=report.html"])
    pytest.main(["-s", "test_expectation.py"])