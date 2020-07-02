# test_02.py
# coding:utf-8
import pytest

#** 作者：上海-悠悠 QQ交流群：588402570**

# 测试账号数据
test_user_data = ["admin1", "admin2"]

@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户：%s"%user)
    return user

@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a != ""


if __name__ == "__main__":
    pytest.main(["-s", "test_02.py", '--alluredir', './report/xml'])

    import os
    # 当前目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 项目根目录
    rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]

    # import pdb; pdb.set_trace()
    xml_report_path = rootPath + r'report\xml'
    html_report_path = rootPath + r'report\html'
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=xml_report_path, html_report_path=html_report_path)).read()






