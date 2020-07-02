#! /usr/bin/env python
# -*- coding: utf-8 -*-

from jira import JIRA
"""
summary：格式 内容 [crash/error/caton] 内容
priority：发生次数和定级关联，定级和解决期限fix_day关联
assignee：统一指派 or
components：新建分类
versions：根据最新问题版本分类？jira无对应版本时
"""

def create_issue(log_info, ):
    """
    :param log_info: (account,password)
    :param project: 项目名称   eg: SQEAP https://jira.nevint.com/browse/SQEAP-483
    :param issuretype: 选择范围：Bug、Story、Epic、Task、Sub-task  具体看项目
    :param priority: 选择范围：P1 - Critical、P2 - High、P3 - Medium、P4 - Low、P5 - Undetermined
    :param summary: issue标题
    :param versions:iusse对应版本 Affects Version/s  选择范围见新建issue Affects Version选项
    :param customfield_10903: 发现方式  How Found 选择范围见新建issue How Found选项
    :param components:选择范围见新建issue Component选项
    :param assignee: 指派人账号（邮箱前缀）
    :param description: issue描述
    :param attachment: 附件的本地连接
    :param fix_day: 解决问题所需天数(工作日)
    :return:
    """
    options = {'server': 'https://jira.xxx.com/'}
    jira = JIRA(options, basic_auth=log_info)
    now = datetime.datetime.now().date()
    fix_day = 3
    end_day = now + datetime.timedelta(days=1)
    while fix_day > 0:  # 在创建日基础上增加预期的工作日
        end_day += datetime.timedelta(days=1)
        if end_day.weekday() not in [0, 1, 2, 3, 4]:
            continue
        else:
            fix_day -= 1
    issue_dict = {
        'project': {'key': 'SQEAP'},  # 项目
        'issuetype': {'name': 'Bug'},  # 问题类型
        'priority': {'name': 'P3 - Medium'},  # 优先级
        'summary': '自动化创建jira测试',  # 问题主题
        'versions': [{'name': '123'}],  # 解决版本
        'customfield_10903': {'value': 'Automation'},  # 发现方式
        'components': [{"name": "aaa"}],  # 相关模块
        'assignee': {'name': 'xxx'},  # 经办人
        'description': '自动化创建jira测试',  # 问题描述
        'customfield_10300': str(now),  # 计划开始时间
        'customfield_10405': str(end_day),  # 计划结束时间
    }
    rsp = jira.create_issue(issue_dict)
    issue = jira.issue(rsp)
    jira.add_attachment(issue=issue, attachment='pytest_learn.zip')
    jira.close()



def create_issue_eddid(log_info, title):
    options = {'server': 'http://172.16.10.243:8080/'}
    jira = JIRA(options, basic_auth=log_info)

    summary = "[新老版本对比][委托下单]{}".format(title)
    description = '''
    [请求参数]
    {
        "MF": 301,
        "thread_id": {{thread_id}},
        "fund_account": "",
        "exchange_type": "K",
        "stock_account": "3001331112",
        "stock_code": "00008",
        "entrust_amount": 10000,    
        "entrust_price": 0.047,
        "entrust_bs": "B",
        "entrust_prop": "e",
        "op_station": "isX5db4FstXj2MdW3weZGcpAktjHG4nM",
        "session_no": {{session_no}}
    }

    [老接口响应数据]
    {'error_no': -9999, 'error_info': '用户编号或密码无效', 'error_info_ansi': '�û���Ż�������Ч'}

    [新接口响应数据]
    {'error_no': -1, 'error_info': '由于长时间未操作或其他原因，为确保您的交易安全，请重新登录.', 'error_info_ansi': '���ڳ�ʱ��δ����������ԭ��Ϊȷ�����Ľ��װ�ȫ�������µ�¼.'}

    [期望结果]
    新老接口, 响应数据一致

    '''

    issue_dict = {
        'project': {'key': 'AYER'},  # 项目
        'issuetype': {'id': '10004'},  # 问题类型
        'priority': {'id': '3'},  # 优先级
        'summary': summary,  # 问题主题
        'assignee': {'name': 'wuchaozhen'},  # 经办人
        'description': description,  # 问题描述
        'customfield_10203' : {'id' : '10112'},
    }
    rsp = jira.create_issue(issue_dict)
    issue = jira.issue(rsp)
    print(issue.key, issue.fields.summary, issue.fields.status)
    jira.close()


def test_jira():
    options = {'server': 'http://172.16.10.243:8080/'}
    jira = JIRA(options, basic_auth=("zhengqinyuan", "12345678"))

    issue = jira.search_issues('project=AYER')
    # print(issue)
    isss = jira.issue("AYER-64")
    # print(isss.fields.issuetype)
    # print(isss.fields.priority)
    # print(isss.fields.customfield_10203)
    allfields = isss.fields()
    meta = jira.editmeta(issue)


# test_jira()


create_issue_eddid(("zhengqinyuan", "12345678"), "测试数据")